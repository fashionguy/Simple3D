from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.5, 1, 1, 0)
    glutWireTeapot(0.5)
    # glutSolidTeapot(0.5)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowPosition(0, 0)
glutInitWindowSize(400, 400)
glutCreateWindow("第一个OpenGL程序--犹他茶壶".encode('cp936'))
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
