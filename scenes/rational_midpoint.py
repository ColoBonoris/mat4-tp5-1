from manim import *

class RationalMidpoint(Scene):
    def construct(self):
        # Define los puntos a y b
        a, b = -2, 3  # Ejemplo de valores racionales
        x = (a + b) / 2  # Punto medio

        # Crear la recta numérica
        number_line = NumberLine(
            x_range=[-3, 4, 1],
            length=10,
            include_numbers=True
        )
        self.play(Create(number_line))

        # Marcar a, b y x en la recta
        a_dot = Dot(number_line.n2p(a), color=BLUE_C)
        b_dot = Dot(number_line.n2p(b), color=RED_C)
        x_dot = Dot(number_line.n2p(x), color=GREEN_C)

        a_label = MathTex("a").next_to(a_dot, DOWN * 3)
        b_label = MathTex("b").next_to(b_dot, DOWN * 3)
        x_label = MathTex("x=\\frac{a+b}{2}").next_to(x_dot, UP)

        self.play(FadeIn(a_dot, b_dot))
        self.play(Write(a_label), Write(b_label))
        
        # Mostrar la existencia de x
        self.wait(1)
        self.play(FadeIn(x_dot), Write(x_label))
        
        # Destacar la desigualdad a < x < b
        inequality = MathTex("a < x < b").to_edge(UP)
        self.play(Write(inequality))
        
        self.wait(2)
