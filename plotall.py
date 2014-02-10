import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sys

def plot(fn):
  with open(fn, 'r') as inp:
    header = inp.readline().strip().split(',')
    
  data = np.genfromtxt(fn, delimiter=',', skip_header=1,
                       skip_footer=0, names=header)
  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Fred vs Dock6")    
  ax1.set_xlabel('Dock6 gear score')
  ax1.set_ylabel('Fred cg4')
  #ax1.plot(data['gs'], data['cg4'], color='r', label='the data')
  #ax1.scatter(data['gs'],data['cg4'],label='dock6', color='blue')
  
  for i, res in enumerate(data['result']):
    if res == 1:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='blue')
    #else:
      #ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
  
  ##ax1.scatter(data['gs'],data['cg4'], c = data['result'],label='dock6', cmap = cm.jet) #maybe not right
  plt.xlim((-50,50))
  #plt.xlim((-200,1200))
  plt.ylim((-12,4))
  plt.savefig('reszoom'+fn+'.png', bbox_inches=0)

  for i, res in enumerate(data['result']):
    if res != 1:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
  plt.savefig('bothzoom'+fn+'.png', bbox_inches=0)
  
  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Fred vs Dock6")    
  ax1.set_xlabel('Dock6 gear score')
  ax1.set_ylabel('Fred cg4')
  plt.xlim((-50,50))
  plt.ylim((-12,4))
  for i, res in enumerate(data['result']):
    if res != 1:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
  plt.savefig('noreszoom'+fn+'.png', bbox_inches=0)
  
def plotclean(fn):
  with open(fn, 'r') as inp:
    header = inp.readline().strip().split(',')
    
  data = np.genfromtxt(fn, delimiter=',', skip_header=1,
                       skip_footer=0, names=header)
  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Fred vs Dock6")    
  ax1.set_xlabel('Dock6 gear score')
  ax1.set_ylabel('Fred cg4')
  
  for i, res in enumerate(data['result']):
    if res == 1:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='blue')
    else:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
  
  plt.xlim((-50,50))
  plt.ylim((-12,4))
  plt.savefig('bothzoom'+fn+'.png', bbox_inches=0)

def plotthree(fn, z):
  with open(fn, 'r') as inp:
    header = inp.readline().strip().split(',')
    
  data = np.genfromtxt(fn, delimiter=',', skip_header=1,
                       skip_footer=0, names=header)
  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Fred vs Dock6")    
  ax1.set_xlabel('Dock6 gear score')
  ax1.set_ylabel('Fred cg4')
  
  for i, res in enumerate(data['result']):
    if res == 1:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='blue')
    elif res == 0:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
    else:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='green')
  zoom = ''
  plt.xlim((-200,1200))
  if z:
    plt.xlim((-50,50))
    zoom = 'zoom'
  plt.ylim((-12,4))
  filename = 'three' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)

def ploteach(fn, z):
  with open(fn, 'r') as inp:
    header = inp.readline().strip().split(',')
    
  data = np.genfromtxt(fn, delimiter=',', skip_header=1,
                       skip_footer=0, names=header)
  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Fred vs Dock6")    
  ax1.set_xlabel('Dock6 gear score')
  ax1.set_ylabel('Fred cg4')
  
  for i, res in enumerate(data['result']):
    if res == 1:
      response = ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='blue')
    #elif res == 0:
      #ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
    #else:
      #ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='green')
  zoom = ''
  plt.xlim((-200,1200))
  if z:
    plt.xlim((-50,50))
    zoom = 'zoom'
  plt.ylim((-12,4))
  ax1.legend((response), ('response'))#, scatterpoints = 1
  filename = 'single-response' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)
  return
  ##
  for i, res in enumerate(data['result']):
    if res != 1:
      noresponse = ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')

  filename = 'single-both' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)

 

  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Fred vs Dock6")    
  ax1.set_xlabel('Dock6 gear score')
  ax1.set_ylabel('Fred cg4')
  
  for i, res in enumerate(data['result']):
    if res != 1:
      ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
  zoom = ''
  plt.xlim((-200,1200))
  if z:
    plt.xlim((-50,50))
    zoom = 'zoom'
  plt.ylim((-12,4))
  filename = 'single-noresponse' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)

def ploteachdock6(fn, z):
  with open(fn, 'r') as inp:
    header = inp.readline().strip().split(',')
    
  data = np.genfromtxt(fn, delimiter=',', skip_header=1,
                       skip_footer=0, names=header)
  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Dock6 gs vs ligand")    
  ax1.set_xlabel('ligand csid')
  ax1.set_ylabel('Dock6 gs')
  
  for i, res in enumerate(data['result']):
    if res == 1:
      ax1.scatter(data['compoundstate_id'][i],data['gs'][i],label='dock6', color='blue')
    #elif res == 0:
      #ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='red')
    #else:
      #ax1.scatter(data['gs'][i],data['cg4'][i],label='dock6', color='green')
  zoom = ''
  ##plt.xlim((-200,1200))
  if z:
    ##plt.xlim((-50,50))
    zoom = 'zoom'
  ##plt.ylim((-12,4))
  plt.ylim((-50,50))
  filename = 'eres' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)

  for i, res in enumerate(data['result']):
    if res != 1:
      ax1.scatter(data['compoundstate_id'][i],data['gs'][i],label='dock6', color='red')
  filename = 'eboth' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)

 

  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.set_title("Dock6 gs vs ligand")    
  ax1.set_xlabel('ligand csid')
  ax1.set_ylabel('Dock6 gs')
  
  for i, res in enumerate(data['result']):
    if res != 1:
      ax1.scatter(data['compoundstate_id'][i],data['gs'][i],label='dock6', color='red')
  zoom = ''
  ##plt.xlim((-200,1200))
  if z:
    ##plt.xlim((-50,50))
    zoom = 'zoom'
  plt.ylim((-50,50))
  filename = 'enores' + zoom + fn + '.png'
  plt.savefig(filename, bbox_inches=0)



if __name__ == '__main__':
  fn = sys.argv[1]
  #fn = '14.1.31all.csv'
  #fn = 'res14.1.31.csv'

  z = True
  z = False

  #plot(fn)
  #plotclean(fn)
  #plotthree(fn, z)
  ploteach(fn, z)
  z = True
  ploteach(fn, z)
  #ploteachdock6(fn, z)
