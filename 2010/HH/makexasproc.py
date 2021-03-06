#!/usr/bin/python
#-------------------------------------------------------------
# A little program which generates an example XAS processed data
# file with purely invented data.
#
# copyright: Do not even consider to bother me
#
# Mark Koennecke, October 2010
#-------------------------------------------------------------

#------ Python blabla where it finds its stuff......
import sys
sys.path.append('/afs/psi.ch/project/sinq/sl5/lib/python')
sys.path.append('/afs/psi.ch/project/sinq/sl5/lib/python2.4/site-packages')

import nxs,numpy

def makeTextData(outf, name, value):
    outf.makedata(name,'char',[len(value)])
    outf.opendata(name)
    outf.putdata(value)
    outf.closedata()


def putArrayData(outf,name, ardata):
    outf.makedata(name,ardata.dtype.name,ardata.shape)
    outf.opendata(name)
    outf.putdata(ardata)
    outf.closedata()

def makeStink(outf, targetpath, topath):
    outf.openpath(targetpath)
    id = outf.getdataID()
    outf.openpath(topath)
    outf.makelink(id)

#------------------- open file
outf = nxs.open('nxxasproc.hdf','w5')

#---------------- entry
outf.makegroup('entry','NXentry')
outf.opengroup('entry','NXentry')
makeTextData(outf,'title','CucumberOxid')
makeTextData(outf,'definition','NXxasproc')
outf.opendata('definition')
data = 'http://svn.nexusformat.org/definitions/NXxasproc.nxdl.xml'
outf.putattr('URL',data)
outf.closedata()

#--------------- processing group
outf.makegroup('absorption','NXprocess')
outf.opengroup('absorption','NXprocess')
makeTextData(outf,'program','wonder-xas')
makeTextData(outf,'version','3.3.7')
outf.makegroup('parameters','NXparameters')
outf.opengroup('parameters','NXparameters')
makeTextData(outf,'raw_file','nxsasraw.hdf')
outf.closegroup()
outf.closegroup()

#------------------- sample group
outf.makegroup('sample','NXsample')
outf.opengroup('sample','NXsample')
makeTextData(outf,'name','CucumberOxid')
outf.closegroup()

#--------- data group
outf.makegroup('data','NXdata')
outf.opengroup('data','NXdata')
data = numpy.ones((1024),numpy.dtype('float32'))
data.fill(.78)
putArrayData(outf,'wavelength',data)
data = numpy.ones((1024),numpy.dtype('int32'))
data.fill(500)
putArrayData(outf,'data',data)
outf.opendata('data')
data = 'wavelength'
outf.putattr('axes',data)
outf.closedata()
outf.closegroup() # data
outf.closegroup() # entry



outf.close()
