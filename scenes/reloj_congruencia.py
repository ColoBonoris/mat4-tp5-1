from manim import *

class RelojCongruencia(Scene):
    def construct(self):
        radius = 3
        centro = ORIGIN

        reloj = Circle(radius=radius, color=WHITE)
        self.play(Create(reloj))

        # números del reloj
        numeros = VGroup()
        for i in range(1, 13):
            angle = 2 * PI * (i / 12)
            pos = radius * 0.85 * np.array([np.sin(angle), np.cos(angle), 0])
            num = Text(str(i), font_size=30).move_to(pos)
            numeros.add(num)
        self.play(Write(numeros))

        # flecha
        current = 4
        flecha = Arrow(centro, numeros[current % 12 - 1].get_center(), buff=0.1, color=YELLOW)
        self.play(GrowArrow(flecha))

        # simula sumar 7 varias veces y muestra que siempre cae en la misma clase módulo 12
        pasos = 5
        for _ in range(pasos):
            next_num = (current + 7) % 12
            if next_num == 0:
                next_num = 12
            nueva_pos = numeros[next_num - 1].get_center()
            nueva_flecha = Arrow(centro, nueva_pos, buff=0.1, color=YELLOW)
            self.play(Transform(flecha, nueva_flecha), run_time=1)
            current = next_num
            self.wait(0.5)

        congruencia = MathTex("4 \\equiv 11 \\equiv 6 \\equiv 1 \\equiv 8", "\\mod{12}")
        congruencia.to_edge(DOWN)
        self.play(Write(congruencia))
        self.wait(2)
