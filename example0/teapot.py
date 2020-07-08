from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 5, 5, 0)
    glutWireTeapot(0.5)
    # 绘制实心茶壶
    # glutSolidTeapot(0.5)
    # 半径，经线方向的划分，纬线方向的划分
    # glutWireSphere(0.5, 60, 2)
    glFlush()


# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置及大小
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(800, 800)
    # 创建窗口
    glutCreateWindow("CSDN Eastmount")
    # 调用display()函数绘制图像
    glutDisplayFunc(drawFunc)
    # 设置全局的回调函数
    # 当没有窗口事件到达时,GLUT程序功能可以执行后台处理任务或连续动画
    glutIdleFunc(drawFunc)
    # 进入glut主循环
    glutMainLoop()
