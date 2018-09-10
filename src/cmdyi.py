import argparse, sys
import time, logging
import Yi4kAPI

from importlib import import_module

class yiCmd():
	#set order
	cmdA= (
		Yi4kAPI.stopRecording,
		Yi4kAPI.getFileList,
		Yi4kAPI.getSettings,

		Yi4kAPI.getVideoResolution,
		Yi4kAPI.getPhotoResolution,
		Yi4kAPI.getPhotoWhiteBalance,
		Yi4kAPI.getVideoWhiteBalance,
		Yi4kAPI.getPhotoISO,
		Yi4kAPI.getVideoISO,
		Yi4kAPI.getPhotoExposureValue,
		Yi4kAPI.getVideoExposureValue,
		Yi4kAPI.getPhotoShutterTime,
		Yi4kAPI.getVideoSharpness,
		Yi4kAPI.getPhotoSharpness,
		Yi4kAPI.getVideoFieldOfView,
		Yi4kAPI.getRecordMode,
		Yi4kAPI.getCaptureMode,
		Yi4kAPI.getMeteringMode,
		Yi4kAPI.getVideoQuality,
		Yi4kAPI.getVideoColorMode,
		Yi4kAPI.getPhotoColorMode,
		Yi4kAPI.getElectronicImageStabilizationState,
		Yi4kAPI.getAdjustLensDistortionState,
		Yi4kAPI.getVideoMuteState,
		Yi4kAPI.getVideoTimestamp,
		Yi4kAPI.getPhotoTimestamp,
		Yi4kAPI.getLEDMode,
		Yi4kAPI.getVideoStandard,
		Yi4kAPI.getTimeLapseVideoInterval,
		Yi4kAPI.getTimeLapsePhotoInterval,
		Yi4kAPI.getTimeLapseVideoDuration,
		Yi4kAPI.getScreenAutoLock,
		Yi4kAPI.getAutoPowerOff,
		Yi4kAPI.getVideoRotateMode,
		Yi4kAPI.getBuzzerVolume,
		Yi4kAPI.getLoopDuration,


		Yi4kAPI.setDateTime,
		Yi4kAPI.setSystemMode,
		Yi4kAPI.setVideoResolution,
		Yi4kAPI.setPhotoResolution,
		Yi4kAPI.setPhotoWhiteBalance,
		Yi4kAPI.setVideoWhiteBalance,
		Yi4kAPI.setPhotoISO,
		Yi4kAPI.setVideoISO,
		Yi4kAPI.setPhotoExposureValue,
		Yi4kAPI.setVideoExposureValue,
		Yi4kAPI.setPhotoShutterTime,
		Yi4kAPI.setVideoSharpness,
		Yi4kAPI.setPhotoSharpness,
		Yi4kAPI.setVideoFieldOfView,
		Yi4kAPI.setRecordMode,
		Yi4kAPI.setCaptureMode,
		Yi4kAPI.setMeteringMode,
		Yi4kAPI.setVideoQuality,
		Yi4kAPI.setVideoColorMode,
		Yi4kAPI.setPhotoColorMode,
		Yi4kAPI.setElectronicImageStabilizationState,
		Yi4kAPI.setAdjustLensDistortionState,
		Yi4kAPI.setVideoMuteState,
		Yi4kAPI.setVideoTimestamp,
		Yi4kAPI.setPhotoTimestamp,
		Yi4kAPI.setLEDMode,
		Yi4kAPI.setVideoStandard,
		Yi4kAPI.setTimeLapseVideoInterval,
		Yi4kAPI.setTimeLapsePhotoInterval,
		Yi4kAPI.setTimeLapseVideoDuration,
		Yi4kAPI.setScreenAutoLock,
		Yi4kAPI.setAutoPowerOff,
		Yi4kAPI.setVideoRotateMode,
		Yi4kAPI.setBuzzerVolume,
		Yi4kAPI.setLoopDuration,

		Yi4kAPI.capturePhoto,
		Yi4kAPI.startRecording
	)

	def __init__(self, _ip):
		cParser= argparse.ArgumentParser(description='Yi 4k remote control. v1.2')

		for cmd in Yi4kAPI.commands:
			if cmd.values:
				limitZip= list(zip(range(0,len(cmd.values)), cmd.values))
				cParser.add_argument(('-%s' % cmd.commandName),
					choices=list(str(a) for a,b in limitZip),
					help=str(dict(limitZip))
				)
			else:
				cParser.add_argument(('-%s' % cmd.commandName))
		self.args=vars(cParser.parse_args())

		self.yi= Yi4kAPI.YiAPI(_ip)
		if not self.yi.sock:
			logging.error('Camera not found')

	def close(self):
		self.yi.close()

	def execute(self, commands={}):
		print("commands : %s" % commands)
		for cCmd in self.cmdA:
			cName= '_'.join( cCmd.commandName.split('-') )
			if cName in commands:
				if cCmd.values:
					res= self.yi.cmd(cCmd, cCmd.values[int(commands[cName])])
					print("%s: %s, %s" % (cName, cCmd.values.index(res),res))
				else:
					res= self.yi.cmd(cCmd, commands[cName])
					print("%s: %s" % (cName, res))

	def listenSetup(self):
		self.yi.setCB("start_video_record", self.listenCB("start_video_record"))
		self.yi.setCB("video_record_complete", self.listenCB("video_record_complete", ('param',)) )
		self.yi.setCB("start_photo_capture", self.listenCB("start_photo_capture"))
		self.yi.setCB("photo_taken", self.listenCB("photo_taken", ('param',)) )
		self.yi.setCB("enter_album", self.listenCB("enter_album"))
		self.yi.setCB("exit_album", self.listenCB("exit_album"))
		self.yi.setCB("battery", self.listenCB("battery", ('param',)) )
		self.yi.setCB("battery_status", self.listenCB("battery_status", ('param',)) )
		self.yi.setCB("adapter", self.listenCB("adapter", ('param',)) )
		self.yi.setCB("adapter_status", self.listenCB("adapter_status", ('param',)) )
		self.yi.setCB("sdcard_format_done", self.listenCB("sdcard_format_done"))
		self.yi.setCB("setting_changed", self.listenCB("setting_changed", ('param', 'value')) )

	def listenCB(self, _name, _params=()):
		def cb(_res):
			paramA= []
			for cParam in _params:
				paramA.append(', %s' % _res[cParam])
			
			print("Event: %s%s" % (_name, ''.join(paramA)))
			try:
				mod = import_module(_name)
			except ImportError:
				print('Error importing module')
				pass
			else:
				print("module loaded")
				self.execute(mod.cmd(_res[cParam]))

		return cb

def main():
	
	logging.basicConfig(filename='test_log.log',level=logging.DEBUG,\
	format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
	
	cmdyi= yiCmd('192.168.1.4')

	# This script only listen to Yi4k
	cmdyi.listenSetup()

	if cmdyi.yi:
		try:
			raw_input("Listening...\n")

		except KeyboardInterrupt:
			None
		
		cmdyi.close()

if __name__ == '__main__':
	main()
