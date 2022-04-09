#!/cds/sw/ds/ana/conda2/inst/envs/ps-4.2.5/bin/python3


import h5py
import numpy as np
import sys
import ArgumentParser

def fillTofs(f,port,ret,run,phen,ens,tofs):
    p = f.create_group('port_%i'%port)
    v = p.create_group('vret_%i'%ret)
    e = v.create_dataset('energies',data = ens,dtype=np.uint16)
    d = v.create_dataset('tofs',data = tofs,dtype=np.uint16)
    d.attrs.create('run',data = run,dtype=np.uint16)
    d.attrs.create('phEn',data = phen,dtype=np.uint16)
    return f

def main():
    if len(sys.argv)<2:
        print('need output .h5 filename')
        return

    fname = sys.argv[1]
    
    with h5py.File(fname,'w') as f:
        energies = [207.23,205.22,203.5,201.13]
        ##  Photon Energies 600 eV
        tofs = [44800,44823,44842,44869]
        fillTofs(f,port=0,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [45286,45313,54340,45377]
        fillTofs(f,port=0,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [46060,46107,46153,46213]
        fillTofs(f,port=0,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [47654,47766,47867,48009]
        fillTofs(f,port=0,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [49535,49789,50022,50377]
        fillTofs(f,port=0,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [38552,38572,38591,38617]
        fillTofs(f,port=1,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [39036,39065,39094,39193]
        fillTofs(f,port=1,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [39867,39866,39910,39969]
        fillTofs(f,port=1,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [41418,41532,41634,41780]
        fillTofs(f,port=1,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [43315,43575,43809,44166]
        fillTofs(f,port=1,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [36370,36391,36411,36438]
        fillTofs(f,port=4,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [36855,36884,36911,36948]
        fillTofs(f,port=4,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [37633,37681,37723,37784]
        fillTofs(f,port=4,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [39235,39350,39449,39601]
        fillTofs(f,port=4,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [41147,41404,41636,41993]
        fillTofs(f,port=4,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [37635,37654,37673,37701]
        fillTofs(f,port=5,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [38119,38147,38174,38210]
        fillTofs(f,port=5,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [38898,38947,38989,39050]
        fillTofs(f,port=5,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [40504,40616,40719,40867]
        fillTofs(f,port=5,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [42409,42669,42905,43265]
        fillTofs(f,port=5,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [37290,37310,37331,37355]
        fillTofs(f,port=12,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [37777,37805,37833,37868]
        fillTofs(f,port=12,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [38560,38605,38652,38713]
        fillTofs(f,port=12,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [40172,40285,40388,40537]
        fillTofs(f,port=12,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [42087,42347,42586,42951]
        fillTofs(f,port=12,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [37349,37370,37388,37416]
        fillTofs(f,port=13,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [37349,37368,37387,37415]
        fillTofs(f,port=13,ret=0,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [37344,37367,37384,37413]
        fillTofs(f,port=13,ret=0,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [37341,37364,37382,37407]
        fillTofs(f,port=13,ret=0,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [37341,37362,37382,37405]
        fillTofs(f,port=13,ret=0,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [38472,38492,38512,38539]
        fillTofs(f,port=14,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [38958,38986,39015,39049]
        fillTofs(f,port=14,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [39738,39786,39831,39891]
        fillTofs(f,port=14,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [41344,41460,41562,41709]
        fillTofs(f,port=14,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [43254,43513,43749,44115]
        fillTofs(f,port=14,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
        tofs = [42886,42906,42924,42951]
        fillTofs(f,port=15,ret=0,run=7,phen=600,ens=energies,tofs=tofs)
        tofs = [43371,43401,43429,43465]
        fillTofs(f,port=15,ret=50,run=8,phen=600,ens=energies,tofs=tofs)
        tofs = [44153,44200,44246,44306]
        fillTofs(f,port=15,ret=100,run=9,phen=600,ens=energies,tofs=tofs)
        tofs = [45761,45874,45978,46124]
        fillTofs(f,port=15,ret=150,run=10,phen=600,ens=energies,tofs=tofs)
        tofs = [47673,47932,48170,48528]
        fillTofs(f,port=15,ret=175,run=11,phen=600,ens=energies,tofs=tofs)
    return

if __name__ == '__main__':
    main()

'''
'''
