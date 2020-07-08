from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 绘制线段，坐标轴
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0)
    glVertex2f(1.0, 0)
    glVertex2f(0, -1.0)
    glVertex2f(0, 1.0)
    glEnd()

    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.3, 0.3)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5, 0.6)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.9, 0.9)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.5, 0.2)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.2, 0.5)
    glEnd()

    glColor3f(0.0, 1.0, 1.0)
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.5, -0.8)
    glVertex2f(-0.2, -0.6)
    glVertex2f(-0.2, -0.3)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.2, -0.6)
    glEnd()

    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("show")
    glutDisplayFunc(display)
    glutMainLoop()


