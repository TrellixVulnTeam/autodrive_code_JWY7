import os
# download and install gdal for gdal_auto.py: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html

#direc = "./input"
#out_direc = "~/Yours/Projects/SDC/dataset/output"
direc = input("Enter input data directory here: ")
out_direc = input("Enter output data directory here: ")
for file in os.listdir(direc):
    name = file[0:-4]
    print(name)
    print("gdal_translate -of JPEG -scale -co worldfile=yes {}/{} {}/{}.jpg".format(direc,file,out_direc,name))
    os.system("gdal_translate -of JPEG -scale -co worldfile=yes {}/{} {}/{}.jpg".format(direc,file,out_direc,name))

for file in os.listdir(out_direc):
    if (file[-3:]!="jpg"):
        os.remove("{}/{}".format(out_direc,file))