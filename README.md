# Hough Transform with OpenCV

This repository is my journey exploring the Hough Circle Transform application using OpenCV and Python. You can check my implementation on the **code folder**.


## Hough Transform Theory

This transform is a feature extraction technique used in images to detect simple geometric forms that can be easily parameterized, such as lines, circles, or ellipses. 

For the desired geometric form, we define an equation to represent it. A line can be described as  <!-- $\rho = x*cos(\theta) + y*sin(\theta)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Crho%20%3D%20x*cos(%5Ctheta)%20%2B%20y*sin(%5Ctheta)">. , for example, then the two parameters:  <!-- $\rho$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Crho"> and <!-- $\theta$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctheta"> defines a space of possibilities for our lines.

What the transform does is map every pixel on our image to a curve in the parameters space. If a point in this space is the intersection of many curves, there is a high probability it describes a line in the image.

### Example

Given an image:

![rho_theta](img/simple_line_wpoints.png)

We get pixels some pixels that are in the line and plot their representation on the parameters space. For this example, we will use the <!-- $\rho = x*cos(\theta) + y*sin(\theta)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Crho%20%3D%20x*cos(%5Ctheta)%20%2B%20y*sin(%5Ctheta)"> representation:
	
![rho_theta](img/rho_theta.png)

The intersection point in this case is <!-- $\theta = \frac{3\pi}{2}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctheta%20%3D%20%5Cfrac%7B3%5Cpi%7D%7B2%7D"> and <!-- $\rho = 0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Crho%20%3D%200">.

<!-- $$
\rho = x*cos(\theta) + y*sin(\theta
)$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Crho%20%3D%20x*cos(%5Ctheta)%20%2B%20y*sin(%5Ctheta%0D"></div>

<!-- $$
0 = x*cos(\frac{3\pi}{2}) + y*sin(\frac{3\pi}{2})
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=0%20%3D%20x*cos(%5Cfrac%7B3%5Cpi%7D%7B2%7D)%20%2B%20y*sin(%5Cfrac%7B3%5Cpi%7D%7B2%7D)%0D"></div>

<!-- $$
x\frac{\sqrt{2}}{2} = y\frac{\sqrt{2}}{2}
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=x%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%20%3D%20y%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%0D"></div>


<!-- $$
x = y
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%20y%0D"></div>

Being <!-- $x = y$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%20y"> the line present in our image

[Here](https://www.youtube.com/watch?v=ebfi7qOFLuo&ab_channel=octaviVision) you can check a visualization way better than my example.

### Others Geometric Forms

This idea extends to other geometric forms, you just have to change the equation that represents it. For a circle, you can define it by the following equation:

<!-- $$
(x-x_c)^2 + (y - y_c)^2 = r^2
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=(x-x_c)%5E2%20%2B%20(y%20-%20y_c)%5E2%20%3D%20r%5E2%0D"></div>

So, you have three parameters to find: <!-- $x_c$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_c">, <!-- $y_c$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y_c"> and <!-- $r$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=r">.

![rho_theta](img/circle.png)
