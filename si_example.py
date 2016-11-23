import submission_tools,CrystalWriter,CrystalRun,PropertiesWriter,PropertiesRun
import local
import os,json


setup={'id':'si',
        'job_record':submission_tools.JobRecord(),
       'crystal':CrystalWriter.CrystalWriter(open("si.cif").read() ),
       'properties':PropertiesWriter.PropertiesWriter() 
         }

setup['crystal'].xml_name="/home/brian/programs/autogenv2/BFD_Library.xml"
setup['crystal'].kmesh=[2,2,2]
setup['crystal'].dftgrid='LGRID'
setup['crystal'].basis_params=[0.3,1,3]
setup['crystal'].tolinteg=[8,8,8,8,16]
setup['crystal'].spin_polarized=False

runcrys=CrystalRun.CrystalRun(local.LocalCrystal(),setup['crystal'])
runprop=PropertiesRun.PropertiesRun()

currwd=os.getcwd()
d=setup['id']
try:
  os.mkdir(d)
except:
  pass
os.chdir(d)

runcrys.run(setup['job_record'])
raise NotImplementedError
runprop.run(setup['job_record'])

print(runcrys.check_status(setup['job_record']))

setup['crystal_output']=runcrys.output()
