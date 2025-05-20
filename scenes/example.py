
from manim import *

class GrupoProductoZ3Z4(Scene):
    def construct(self):
        # Crear la grilla 3x4
        rows, cols = 3, 4
        cell_size = 1
        grid = VGroup()
        for i in range(rows):
            for j in range(cols):
                cell = Square(cell_size)
                cell.move_to(RIGHT * j + DOWN * i)
                coord = MathTex(f"({i},{j})").scale(0.5)
                coord.move_to(cell.get_center())
                grid.add(cell, coord)
        grid.move_to(ORIGIN)
        self.play(Create(grid), run_time=2)

        # Marcar posición inicial (2,3)
        inicio = Dot(point=RIGHT * 3 + DOWN * 2, color=BLUE).scale(1.5)
        label_inicio = MathTex("(2,3)", color=BLUE).scale(0.7)
        label_inicio.next_to(inicio, UP)
        self.play(FadeIn(inicio), Write(label_inicio))

        # Mostrar vector de movimiento (2,2)
        movimiento_label = MathTex("+ (2,2)").scale(0.7).next_to(label_inicio, UP)
        self.play(Write(movimiento_label))

        # Calcular nueva fila y columna con flechas y pasos
        paso1 = MathTex("2 + 2 = 4", "\Rightarrow", "4 \mod 3 = 1").scale(0.7).to_edge(UP)
        paso2 = MathTex("3 + 2 = 5", "\Rightarrow", "5 \mod 4 = 1").scale(0.7).next_to(paso1, DOWN)
        self.play(Write(paso1), run_time=2)
        self.wait(1)
        self.play(Write(paso2), run_time=2)
        self.wait(1)

        # Dibujar flecha desde (2,3) hasta (1,1)
        start = RIGHT * 3 + DOWN * 2
        end = RIGHT * 1 + DOWN * 1
        flecha = Arrow(start, end, buff=0.1, color=GREEN)
        self.play(GrowArrow(flecha), run_time=2)

        # Marcar destino
        destino = Dot(point=end, color=GREEN).scale(1.5)
        label_destino = MathTex("(1,1)", color=GREEN).scale(0.7)
        label_destino.next_to(destino, UP)
        self.play(FadeIn(destino), Write(label_destino))

        # Conclusión
        conclus = MathTex("(2,3) + (2,2) = (1,1)").scale(0.9).to_edge(DOWN)
        self.play(Write(conclus), run_time=2)
        self.wait(2)
