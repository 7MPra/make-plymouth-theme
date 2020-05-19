import os
import shutil
import ffmpeg
import sys

if shutil.which('ffmpeg') == None:
	print('{}: Please install ffmpeg!'.format(sys.argv[0]))
	sys.exit(1)

def usage():
	print('{0}: {0} video_filename theme_name'.format(sys.argv[0]))
	sys.exit(1)

if sys.argv[1] == '-h':
	usage()
if len(sys.argv) != 3:
	usage()
if not os.path.isfile(sys.argv[1]):
	print('{}: Error: {} is not found.'.format(sys.argv[0],sys.argv[1]))
	usage()

if os.path.exists(sys.argv[2]):
	shutil.rmtree(sys.argv[2])
os.makedirs(sys.argv[2])

in_video=sys.argv[1]
out_pic='{}/progress-%d.png'.format(sys.argv[2])
option='-vcodec png --start_number 0'

os.system('ffmpeg -i {} {} {}'.format(in_video,option,out_pic))

filelist = os.listdir('./{}'.format(sys.argv[2]))

plymouth_file = open('{0}/{0}.plymouth'.format(sys.argv[2]),'w')
script_file = open('{0}/{0}.script'.format(sys.argv[2]),'w')

plymouth_file.write('[Plymouth Theme]\n')
plymouth_file.write('Name={0}\n'.format(sys.argv[2]))
plymouth_file.write('Description=This is a Plymouth theme with a {0} animation.\n'.format(sys.argv[2]))
plymouth_file.write('ModuleName=script\n')
plymouth_file.write('\n')
plymouth_file.write('[script]\n')
plymouth_file.write('ImageDir=/usr/share/plymouth/themes/{0}\n'.format(sys.argv[2]))
plymouth_file.write('ScriptFile=/usr/share/plymouth/themes/{0}/{0}.script'.format(sys.argv[2]))

script_file.write('Window.SetBackgroundTopColor (0, 0, 0);\n')
script_file.write('Window.SetBackgroundBottomColor (0, 0, 0);\n')
script_file.write('for (i = 0; i < {}; i++)\n'.format(len(filelist)))
script_file.write('  image[i] = Image("progress-" + i + ".png");\n')
script_file.write('sprite = Sprite();\n')
script_file.write('\n')
script_file.write('sprite.SetX(Window.GetWidth() / 2 - image[0].GetWidth() / 2);\n')
script_file.write('sprite.SetY(Window.GetHeight() / 2 - image[0].GetHeight() / 2);')
script_file.write('\n')
script_file.write('progress = 0;\n')
script_file.write('\n')
script_file.write('fun refresh_callback ()\n')
script_file.write('  {\n')
script_file.write('    sprite.SetImage(image[Math.Int(progress / 2) % {}]);\n'.format(len(filelist)))
script_file.write('    progress++;\n')
script_file.write('  }\n')
script_file.write('Plymouth.SetRefreshFunction (refresh_callback);')
