# ASCII Sphere Ray Tracer

## What It Is
A 3D rendering engine written in Python.

## What It Does
The program renders an animated 3D sphere directly in the terminal using ASCII characters. It simulates a rotating light source to create a real-time lighting and shadow effect on the sphere's surface.

## Math Used
* **3D Vectors:** A custom class was built to handle points and directions in 3D space.
* **Ray-Sphere Intersection:** To detect a "hit," the program solves a **quadratic equation** to find the intersection of a line and a sphere, checking the equation's **discriminant**.
* **Diffuse Lighting:** The brightness of any point on the sphere is calculated using the **dot product** of the surface direction (normal) and the light's direction.
