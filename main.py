
# example.py

from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    def construct(self):
        title = VGroup(
            Text("Runge Kutta", color = BLUE),
            Text("A Numerical Differential Equation Approximator").scale(.8),
            Text("By Alistair Keiller").scale(.6),
        ).arrange(DOWN)
        self.play(Write(title))
        self.next_slide()

        self.play(FadeOut(title))
        t = Text("Deriving RK2").to_edge(UP)
        self.play(Write(t))
        e1 = MathTex(r"y'=f(t,y), y(0)=y_0").move_to(t).shift(DOWN*0.8)
        self.play(Write(e1))
        e2 = MathTex(r"y(t+\Delta t)=y+\Delta t y'+\frac{\Delta t^2}{2}y''").move_to(e1).to_edge(LEFT).shift(DOWN)
        self.play(Write(e2))
        self.next_slide()

        e3 = MathTex(r"y(t+\Delta t)=y+\Delta t f(t,y)+\frac{\Delta t^2}{2}f(t,y)'").move_to(e1).to_edge(LEFT).shift(DOWN)
        self.play(Transform(e2,e3))
        self.next_slide()

        e4 = MathTex(r"y(t+\Delta t)=y+\Delta t f(t,y)+\\\frac{\Delta t^2}{2}[\frac{\partial f(t,y)}{\partial t}+f(t,y)\frac{\partial f(t,y)}{\partial y}]").move_to(e1).to_edge(LEFT).shift(DOWN*2)
        self.play(Transform(e2,e4))
        self.next_slide()

        e5 = MathTex(r"k_1&=\Delta t f(t,y) \\ k_2&=\Delta t f(t+\alpha \Delta t,y+\beta k_1) \\ &y(t+\Delta t)=y+a k_1+b k_2").move_to(e1).to_edge(RIGHT).shift(DOWN*2)
        self.play(Write(e5))
        e6 = MathTex(r"y(t+\Delta t)=a \Delta t f(t,y)+\\ b \Delta t f(t+\alpha \Delta t,y+\beta k_1)").move_to(e5).to_edge(RIGHT).shift(DOWN*2)
        self.play(Write(e6))
        self.next_slide()

        e7 = MathTex(r"y(t+\Delta t)=y+{{(a+b)}}\Delta t f(t,y)+\\ \frac{\Delta t^2}{2}[{{\alpha b}} \frac{\partial f(t,y)}{\partial t}+{{\beta b}} f(t,y)\frac{\partial f(t,y)}{\partial y}]").move_to(e5).to_edge(RIGHT).shift(DOWN*2.3)
        self.play(Transform(e6,e7))
        self.next_slide()

        e8 = MathTex(r"y(t+\Delta t)=y+{{(a+b)}}\Delta t f(t,y)+\\ \frac{\Delta t^2}{2}[{{\alpha b}} \frac{\partial f(t,y)}{\partial t}+{{\beta b}} f(t,y)\frac{\partial f(t,y)}{\partial y}]").move_to(e5).to_edge(RIGHT).shift(DOWN*2.3)
        e8.set_color_by_tex(r"b",RED)
        self.play(Transform(e6,e8))
        self.next_slide()

        self.play(FadeOut(t),FadeOut(e1),FadeOut(e2),FadeOut(e5),FadeOut(e6))
        e9 = MathTex(r"a+b&=1 \\ \alpha b &= \frac{1}{2} \\ \beta b &= \frac{1}{2}").to_edge(UP)
        self.play(Write(e9))
        e10 = MathTex(r"\text{Euler Solution:} \\ a=b=\frac{1}{2} \\ \alpha=\beta=1").move_to(e9).to_edge(LEFT).shift(DOWN*2)
        self.play(Write(e10))
        e11 = MathTex(r"\text{Midpoint Solution:} \\ a=0 \\ b=1 \\ \alpha=\beta=\frac{1}{2}").move_to(e9).to_edge(RIGHT).shift(DOWN*2)
        self.play(Write(e11))
        self.next_slide()

        e12 = MathTex(r"\text{Euler Solution:} \\ k_1=\Delta t f(t,y) \\ k_2=\Delta t f(t+\Delta t, y+k_1) \\ y(t+\Delta t)=y+\frac{1}{2}(k_1+k_2)").move_to(e9).to_edge(LEFT).shift(DOWN*2)
        e13 = MathTex(r"\text{Midpoint Solution:} \\ k_1=\Delta t f(t,y) \\ k_2=\Delta t f(t+\frac{1}{2} \Delta t, y+\frac{1}{2} k_1) \\ y(t+\Delta t)=y+k_2").move_to(e9).to_edge(RIGHT).shift(DOWN*2)
        self.play(FadeOut(e9))
        self.play(Transform(e10,e12))
        self.play(Transform(e11,e13))
        self.next_slide()

        self.play(FadeOut(e10), FadeOut(e11))
        e14 = Text("Case Study: Newtonian Drag").to_edge(UP)
        self.play(Write(e14))
        e15 = MathTex(r"x''&=\mu x' \sqrt{x'^2+y'^2+z'^2} \\ y''&=\mu y' \sqrt{x'^2+y'^2+z'^2} \\ z''&=\mu z' \sqrt{x'^2+y'^2+z'^2}")
        self.play(Write(e15))

        self.next_slide()
        e16 = MathTex(r"a_x&=\mu v_x \sqrt{v_x^2+v_y^2+v_z^2} \\ a_y&=\mu v_y \sqrt{v_x^2+v_y^2+v_z^2} \\ a_z&=\mu v_z \sqrt{v_x^2+v_y^2+v_z^2} \\ x'&=v_x \\ y'&=v_y \\ z'&=v_z")
        self.play(Transform(e15,e16))
        self.next_slide()

        self.play(FadeOut(e14,e15))
        e17 = Text("Case Study: Schrodinger Equation").to_edge(UP)
        self.play(Write(e17))
        e18 = MathTex(r"\frac{\partial \Psi}{\partial t}=-i h H \Psi")
        self.play(Write(e18))
        self.next_slide()

        e19 = MathTex(r"\frac{\partial \Psi}{\partial t}=-i h (V + \nabla^2) \Psi")
        self.play(Transform(e18,e19))
        self.next_slide()
        
        e20 = MathTex(r"\frac{\partial \Psi}{\partial t}=-i h (V + \frac{\partial^2}{\partial^2 x} + \frac{\partial^2}{\partial^2 y}) \Psi")
        self.play(Transform(e18,e20))
