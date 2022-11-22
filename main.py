from SerialAudioDriver import SerialAudioDriver

def main():
  driver = SerialAudioDriver()
  driver.tRead.start()

if __name__ == '__main__':
  main()
