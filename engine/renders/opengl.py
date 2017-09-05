from math import sin, cos
from array import array
from struct import unpack

from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

window_x = 800
window_y = 600

def init_screen():
    'init pygame display'
    pygame.display.init()
    pygame.display.set_mode((int(window_x),int(window_y)), HWSURFACE|OPENGL|DOUBLEBUF,)
    pygame.display.set_caption('Test','Test')

def update_screen():
    'update pygame display'
    pygame.display.flip()

def init_opengl():
    'init openGL'
    glClearColor(0.6,0.6,0.6,1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)
    glEnable(GL_POLYGON_SMOOTH)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glShadeModel(GL_SMOOTH)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

def camera_loop():
    'camera at (22,28,-18) looking at (0,0,0)'
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    gluPerspective(65.0, (window_x/window_y), 0.1, 200.0)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    gluLookAt(  22.0, 28.0, -18.0,
                0.0, 0.0, 0.0,
                0.0, 1.0, 0.0 )

    glViewport(0, 0, window_x, window_y)

def light_loop():
    'light which change position every frame'
    glPushMatrix()
    glDisable(GL_LIGHTING)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor4f(1.0,1.0,1.0,1.0)
    glVertex4fv((0.0,20.0,0.0,1.0))
    glEnd()
    glPopMatrix()

    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0,1.0,1.0,1.0))   # Setup The Diffuse Light
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.6,0.6,0.6,1.0))  # Setup The Specular Light
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1,0.1,0.1,1.0))   # Setup The Ambient Light
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0,20.0,0.0,1.0)) # Position of The Light

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
    glEnable(GL_LIGHT0)

    glEnable(GL_LIGHTING)

def list_file(vtx_file):
    'open vtx_file and create a glList'
    all_vtx_data = array('f')
    mat_attr = array('f')

    f = open(vtx_file, 'rb')
    all_vtx_data.fromfile(f, int(unpack('f',f.read(4))[0])*8 )
    mat_attr.fromfile(f, 11)
    f.close()

    trasparency = mat_attr[3]
    shine = mat_attr[4]

    matAmb = [ 0.05, 0.05, 0.05, 1.0 ]
    matDiff = [mat_attr[0], mat_attr[1], mat_attr[2], trasparency ]
    matSpec = [mat_attr[5], mat_attr[6], mat_attr[7], trasparency ]
    matEmis = [mat_attr[8], mat_attr[9], mat_attr[10], trasparency ]

    id_list = glGenLists(1)
    glNewList (id_list, GL_COMPILE)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiff)
    glMaterialfv(GL_FRONT, GL_AMBIENT, matAmb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, matSpec)
    glMaterialfv(GL_FRONT, GL_EMISSION, matEmis)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)

    glBegin(GL_TRIANGLES)
    for i in range(0, len(all_vtx_data), 8):
        glNormal3fv((all_vtx_data[i+0], all_vtx_data[i+1], all_vtx_data[i+2]))
        glVertex3fv((all_vtx_data[i+5], all_vtx_data[i+6], all_vtx_data[i+7]))
    glEnd()

    glEndList()

    return id_list

def render_floor(listID):
    'render floor'
    glPushMatrix()
    glCallList(listID)
    glPopMatrix()

def render_obj(listID, rot):
    'render (really easy) animated object'
    glPushMatrix()
    glRotate(rot, 0.0, 0.0, 0.0)
    glCallList(listID)
    glPopMatrix()
