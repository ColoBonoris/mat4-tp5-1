import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import os from "os";
import colors from "picocolors";
import { Server as SocketIOServer } from "socket.io";
import { defineConfig } from "vite";

function getLocalNetworkIP() {
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      if (iface.family === "IPv4" && !iface.internal) {
        return iface.address;
      }
    }
  }
  return "localhost";
}

const __dirname = dirname(fileURLToPath(import.meta.url));

function socketIOPlugin() {
  let io;

  return {
    name: "vite-plugin-socketio",
    configureServer(server) {
      io = new SocketIOServer(server.httpServer);

      var host = false;
      var users = 0;

      io.on("connection", function (socket) {
        var user = {
          id: ++users,
        };

        if (host) host.emit("access", user);

        socket.on("host", function (_msg) {
          host = socket;
        });
        socket.on("move", function (msg) {
          if (host) {
            msg.user = user.id;
            host.volatile.emit("move", msg);
          }
        });
        socket.on("touch", function (msg) {
          if (host) {
            host.emit("touch", {
              user: user.id,
              type: msg.type,
            });
          }
        });
        socket.on("slide", function (msg) {
          if (host) {
            host.emit("slide", {
              user: user.id,
              type: msg.type,
            });
          }
        });
        socket.on("zoom", function (msg) {
          if (host) {
            host.emit("zoom", {
              user: user.id,
              type: msg.type,
            });
          }
        });
        socket.on("view", function (msg) {
          if (host) {
            host.emit("view", {
              user: user.id,
            });
          }
        });
        socket.on("disconnect", function (msg) {
          if (host) host.emit("exit", user.id);
        });
      });

      server.httpServer?.once("listening", () => {
        const address = server.config.server.host || "localhost";
        const port = server.config.server.port || 5173;
        const ip = getLocalNetworkIP();

        const colorUrl = (url) =>
          colors.cyan(
            url.replace(/:(\d+)\//, (_, port) => `:${colors.bold(port)}/`)
          );

        const local = `http://${address}:${port}/remote/`;
        const network = `http://${ip}:${port}/remote/`;
        console.log();
        console.info(
          `  ${colors.green("➜")}  ${colors.bold("Remote Local")}:   ${colorUrl(
            local
          )}`
        );
        console.info(
          `  ${colors.green("➜")}  ${colors.bold(
            "Remote Network"
          )}:   ${colorUrl(network)}`
        );
        console.log();
      });
    },
  };
}

export default defineConfig(() => ({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
        remote: resolve(__dirname, "remote/index.html"),
      },
    },
  },
  plugins: [socketIOPlugin()],
}));
