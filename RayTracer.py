import math

import os
import time

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def dot(self, other):
        return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))
    

    def length(self):
        return math.sqrt(self.dot(self))
    
    def normalize(self):
        l = self.length()
        
        if l == 0:
            return Vec3(0, 0, 0)

        return Vec3(self.x / l, self.y / l, self.z / l)
    
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def intersects(self, ray):
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * ray.direction.dot(oc)
        c = oc.dot(oc) - self.radius * self.radius
        discriminant = b*b - 4*a*c

        if discriminant < 0:
            return None
        else:
            t1 = (-b - math.sqrt(discriminant)) / (2.0 * a)
            t2 = (-b + math.sqrt(discriminant)) / (2.0 * a)

            if t1 > 0:
                return t1

            if t2 > 0:
                return t2
            
            return None


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    WIDTH = 80
    HEIGHT = 40
    
    camera = Vec3(0, 0, 0)
    sphere = Sphere(center=Vec3(0, 0, -5), radius=2.0)
    
    gradient = " .:!/r(l1Z4H9W8$@"
    
    angle = 0

    while True:
        clear_screen()
        
        light_x = math.cos(angle) * 5
        light_z = math.sin(angle) * 5
        light = Vec3(light_x, -5, light_z).normalize()
        
        output = ""
        for j in range(HEIGHT):
            line = ""
            for i in range(WIDTH):
                x = (i - WIDTH / 2) / (WIDTH / 2)
                y = -(j - HEIGHT / 2) / (HEIGHT / 2)
                ray = Ray(camera, Vec3(x, y, -1))
                hit_distance = sphere.intersects(ray)

                if hit_distance is None:
                    line += " "
                else:
                    hit_point = ray.origin + ray.direction * hit_distance
                    normal = (hit_point - sphere.center).normalize()
                    brightness = normal.dot(light)
                    if brightness < 0:
                        line += "."
                    else:
                        char_index = int(brightness * (len(gradient) - 1))
                        line += gradient[char_index]
            output += line + "\n"
        
        print(output)
        
        angle += 0.05
        
        time.sleep(0.01)

if __name__ == '__main__':
    main()