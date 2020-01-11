class Amplifier():
    def __init__(self):
        self.cd = None
        self.dvd = None
        self.turner = None

    def on(self):
        print('The amplifier is on.')

    def off(self):
        print('The amplifier is off.')

    def set_CD(self, cd):
        self.cd = cd

    def set_DVD(self, dvd):
        self.dvd = dvd

    def set_stereo_sound(self, volumn):
        print('Set stereo sound {}.'.format(volumn))

    def set_surround_sound(self):
        print('Set surround sound.')

    def set_turner(self,turner):
        self.turner = turner

    def set_volumn(self, volumn):
        print('Set volumn {}.'.format(volumn))


class Turner():
    def __init__(self, amplifier):
        self.amplifier = amplifier

    def on(self):
        print('The turner is on.')

    def off(self):
        print('The turner is off.')

    def set_AM(self):
        print('Set AM...')

    def set_FM(self):
        print('Set FM...')

    def set_frequency(self,frequency):
        print('Set frequency {}.'.format(frequency))


class CD_player():
    def __init__(self, amplifier):
        self.amplifier = amplifier

    def on(self):
        print('The CD player is on.')

    def off(self):
        print('The CD player is off.')

    def eject(self):
        print('The CD is ejected out.')

    def play(self, cd_name):
        print('Start to play {}.'.format(cd_name))

    def pause(self):
        print('Pause')

    def stop(self):
        print('Stop playing...')


class DVD_player():
    def __init__(self, amplifier):
        self.amplifier = amplifier

    def on(self):
        print('The DVD player is on.')
    
    def off(self):
        print('The DVD player is off.')

    def eject(self):
        print('The DVD is ejected out.')

    def play(self, dvd_name):
        print('Start to play {}.'.format(dvd_name))

    def pause(self):
        print('Pause')

    def stop(self):
        print('Stop playing...')

    def set_surround_audio(self):
        print('Set surround audio...')

    def set_two_channel_audio(self):
        print('Set 2 channels audio...')


class Projector():
    def __init__(self, dvd_player):
        self.dvd_player = dvd_player

    def on(self):
        print('The projector is on.')

    def off(self):
        print('The projector is off.')

    def tv_mode(self):
        print('The projector turns to TV mode.')
        
    def wide_screen_mode(self):
        print('The projector turns to wide screen mode.')


class PopcornPopper():
    def on(self):
        print('The popcorn popper is on.')
            
    def off(self):
        print('The popcorn popper is off.')

    def pop(self):
        print('The popcorn popper starts to pop.')


class Screen():
    def up(self):
        print('The screen is up.')

    def down(self):
        print('The screen is down.')


class TheaterLights():
    def on(self):
        print('The theater lights are on.')

    def off(self):
        print('The theater lights are off.')

    def dim(self, dim=10):
        print('Set lights dim to {}.'.format(dim))


class HomeTheaterFacade():
    def __init__(self, amp, dvd, cd, turner, proj, screen, lights, pop):
        self.amp = amp
        self.dvd = dvd
        self.cd = cd
        self.turner = turner
        self.proj = proj
        self.screen = screen
        self.lights = lights
        self.pop = pop

    def watch_movie(self, movie):
        print('Start to watch movie...')
        self.pop.on()
        self.pop.pop()
        self.lights.dim(10)
        self.screen.down()
        self.proj.on()
        self.proj.wide_screen_mode()
        self.amp.on()
        self.amp.set_DVD(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volumn(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print('End movie...')
        self.pop.off()
        self.lights.on()
        self.screen.up()
        self.proj.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

# listen_to_CD()
# end_CD()
# listen_to_radio()
# end_radio()

if __name__ == '__main__':
    amp = Amplifier() 
    dvd = DVD_player(amp) 
    cd = CD_player(amp) 
    turner = Turner(amp) 
    proj = Projector(dvd) 
    screen = Screen()
    lights = TheaterLights() 
    pop = PopcornPopper()

    home_theater = HomeTheaterFacade(amp, dvd, cd, turner, proj, screen, lights, pop)
    home_theater.watch_movie('Movie Name')
    home_theater.end_movie()