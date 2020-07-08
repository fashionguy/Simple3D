from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex3f(-0.5, -0.5, 0.0)
    glColor3f(0, 1, 0)
    glVertex3f(0.5, -0.5, 0.0)
    glColor3f(1, 0, 0)
    glVertex3f(0.5, 0.5, 0.0)
    glColor3f(0, 1, 0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow('my')
    glutDisplayFunc(display)
    glutMainLoop()

