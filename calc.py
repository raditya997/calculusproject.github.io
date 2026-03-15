from manim import *
import numpy as np

class OptimalSolution(Scene):
    def construct(self):

        # Title
        title = Text("Optimization of Boat Efficiency", font_size=40)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Efficiency function
        func_text = MathTex(
            "E(x) = x(10 - x)^2"
        )
        func_text.next_to(title, DOWN)

        self.play(Write(func_text))
        self.wait(2)

        # Expand the function
        expansion = MathTex(
            "E(x) = x(100 - 20x + x^2)"
        )
        expansion.next_to(func_text, DOWN)

        # self.play(Transform(func_text.copy(), expansion))
        self.play(Write(expansion))
        self.wait(2)

        simplified = MathTex(
            "E(x) = 100x - 20x^2 + x^3"
        )
        simplified.next_to(expansion, DOWN)

        self.play(Write(simplified))
        self.wait(2)

        # Derivative step
        derivative_title = Text("First Derivative", font_size=30)
        derivative_title.to_edge(LEFT).shift(DOWN)

        self.play(Write(derivative_title))

        derivative = MathTex(
            "E'(x) = 100 - 40x + 3x^2"
        )
        derivative.next_to(derivative_title, RIGHT)

        self.play(Write(derivative))
        self.wait(2)

        # Set derivative = 0
        critical = MathTex(
            "100 - 40x + 3x^2 = 0"
        )
        critical.next_to(derivative, DOWN)

        self.play(Write(critical))
        self.wait(2)

        # Solution expression
        solution = MathTex(
            "x = 10 - \\frac{12}{\\sqrt{65}}"
        )
        solution.next_to(critical, DOWN)

        self.play(Write(solution))
        self.wait(2)

        # Approximation
        approx = MathTex(
            "x \\approx 8.51"
        )
        approx.next_to(solution, DOWN)

        self.play(Write(approx))
        self.wait(2)
        self.play(FadeOut(title, func_text, simplified, derivative, derivative_title, solution, critical, expansion, approx
                          ))

        # Graph Section
        graph_title = Text("Graph of Efficiency Function", font_size=30)
        graph_title.to_edge(DOWN)

        self.play(Write(graph_title))

        axes = Axes(
            x_range=[0, 12, 1],
            y_range=[0, 400, 50],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True},
        )

        axes.to_edge(DOWN)

        labels = axes.get_axis_labels(x_label="x", y_label="E(x)")

        graph = axes.plot(
            lambda x: x*(10-x)**2,
            x_range=[0,10],
            color=BLUE
        )

        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.wait(2)

        # Optimal point
        x_opt = 8.51
        y_opt = x_opt*(10-x_opt)**2

        dot = Dot(
            axes.coords_to_point(x_opt, y_opt),
            color=RED
        )

        label = MathTex(
            "x \\approx 8.51"
        ).next_to(dot, RIGHT)

        self.play(FadeIn(dot), Write(label))
        self.wait(3)

        # Highlight optimum
        optimum_text = Text(
            "Optimal Solution Achieved",
            font_size=35,
            color=YELLOW
        )

        optimum_text.to_edge(UP)

        self.play(Write(optimum_text))
        self.wait(3)
        self.play(FadeOut(graph_title, axes, labels, graph, dot, label, optimum_text))

        # TITLE
        title = Text("From Geometry to Optimization", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, LEFT))
       

        shore = Line(LEFT*5, RIGHT*5)
        self.play(Create(shore))

   
        house = Dot(LEFT*4)
        run_point = Dot(LEFT*1)
        closest = Dot(RIGHT*3)
        island = Dot(RIGHT*3 + UP*3)

        self.play(FadeIn(house), FadeIn(run_point), FadeIn(closest), FadeIn(island))

      
        house_label = Text("House", font_size=24).next_to(house, DOWN)
        island_label = Text("Island", font_size=24).next_to(island, UP)

        self.play(Write(house_label), Write(island_label))

   
        run_line = Line(house, run_point, color=BLUE)
        run_label = MathTex("x").next_to(run_line, DOWN)

        self.play(Create(run_line), Write(run_label))

      
        beach_line = Line(run_point, closest, color=GREEN)
        beach_label = MathTex("10-x").next_to(beach_line, DOWN)

        self.play(Create(beach_line), Write(beach_label))

       
        offshore = Line(closest, island, color=YELLOW)
        offshore_label = MathTex("3").next_to(offshore, RIGHT)

        self.play(Create(offshore), Write(offshore_label))

        # BOAT PATH (HYPOTENUSE)
        boat_line = Line(run_point, island, color=RED)

        boat_label = MathTex(
            "\\sqrt{(10-x)^2 + 3^2}"
        ).next_to(boat_line, RIGHT)

        self.play(Create(boat_line), Write(boat_label))
        self.wait(2)

        # TRIANGLE HIGHLIGHT
        triangle = Polygon(
            run_point.get_center(),
            closest.get_center(),
            island.get_center(),
            color=WHITE
        )

        self.play(Create(triangle))
        self.wait(1)

        # PYTHAGOREAN FORMULA
        pythag = MathTex(
            "d = \\sqrt{(10-x)^2 + 3^2}"
        ).to_edge(DOWN)

        self.play(Write(pythag))
        self.wait(2)
        self.play(FadeOut(title, shore, house_label, house, run_point, closest, island, 
                          island_label, run_line, run_label, beach_line, beach_label, offshore, offshore_label, boat_line, boat_label, triangle, pythag))

        # TRANSFORM INTO TIME FUNCTION
        time_title = Text("Time Function", font_size=40)
        self.play(Write(time_title))
        self.wait(1)
        self.play(time_title.animate.to_edge(RIGHT))
       

        time_func = MathTex(
            "T(x) = \\frac{x}{9} + \\frac{\\sqrt{(10-x)^2 + 9}}{4}"
        ).to_edge(DOWN)

        self.play(Transform(pythag, time_func))
        self.wait(2)

        # MOVE FUNCTION TO CORNER
        self.play(pythag.animate.to_corner(UL))

        # CREATE GRAPH
        axes = Axes(
            x_range=[0,10,1],
            y_range=[0,4,0.5],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True}
        )

        axes.to_edge(DOWN)

        graph = axes.plot(
            lambda x: x/9 + np.sqrt((10-x)**2 + 9)/4,
            x_range=[0,10],
            color=BLUE
        )

        self.play(Create(axes))
        self.play(Create(graph))

        # OPTIMAL POINT
        x_opt = 8.51
        y_opt = x_opt/9 + np.sqrt((10-x_opt)**2 + 9)/4

        dot = Dot(
            axes.coords_to_point(x_opt, y_opt),
            color=RED
        )

        label = MathTex("x \\approx 8.51").next_to(dot, RIGHT)

        self.play(FadeIn(dot), Write(label))
        self.wait(3)