from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from textinputlinenumber import TextInputLineNumber


class ExampleRoot(BoxLayout):
    lni = ObjectProperty(None)
    text = StringProperty("")

    def append_lorem_ipsum(self):
        t = (R'''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In ante metus dictum at tempor commodo ullamcorper a lacus. Amet mauris commodo quis imperdiet massa tincidunt nunc. Amet cursus sit amet dictum sit amet justo donec enim. Eget velit aliquet sagittis id consectetur. Blandit libero volutpat sed cras ornare arcu. Mattis nunc sed blandit libero volutpat. Ultrices vitae auctor eu augue ut. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit. Aenean vel elit scelerisque mauris pellentesque.

    Nibh sit amet commodo nulla facilisi nullam vehicula. Tempus quam pellentesque nec nam aliquam sem et. Suspendisse potenti nullam ac tortor vitae purus faucibus ornare suspendisse. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus non. Risus quis varius quam quisque id diam vel quam elementum. Eu non diam phasellus vestibulum lorem sed risus ultricies tristique. Nunc mattis enim ut tellus elementum sagittis vitae. Mi sit amet mauris commodo quis imperdiet. Faucibus turpis in eu mi bibendum neque. Ipsum consequat nisl vel pretium. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada nunc. Ac turpis egestas maecenas pharetra convallis posuere morbi leo urna. Amet porttitor eget dolor morbi non.

    Elementum curabitur vitae nunc sed velit. At urna condimentum mattis pellentesque id nibh tortor id. Ultrices tincidunt arcu non sodales neque sodales. Ante metus dictum at tempor. Consequat semper viverra nam libero. Varius sit amet mattis vulputate enim nulla aliquet porttitor lacus. Suscipit tellus mauris a diam maecenas sed. Nulla pellentesque dignissim enim sit. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus interdum. Justo eget magna fermentum iaculis eu non diam phasellus. Volutpat est velit egestas dui id ornare arcu.

    Aliquam sem et tortor consequat id. Sed vulputate odio ut enim. Eget velit aliquet sagittis id consectetur purus ut faucibus pulvinar. Convallis a cras semper auctor neque vitae tempus quam. Consequat nisl vel pretium lectus quam id leo in. Porta non pulvinar neque laoreet suspendisse interdum. Purus faucibus ornare suspendisse sed nisi lacus sed viverra tellus. Venenatis tellus in metus vulputate eu. Arcu non odio euismod lacinia at. Ut ornare lectus sit amet est placerat in egestas. Sapien pellentesque habitant morbi tristique senectus et netus et malesuada. Dignissim convallis aenean et tortor at risus viverra. Nisl pretium fusce id velit ut tortor pretium viverra suspendisse. Pellentesque nec nam aliquam sem et. Integer vitae justo eget magna fermentum.

    Amet commodo nulla facilisi nullam vehicula ipsum. Ultrices neque ornare aenean euismod elementum. Etiam sit amet nisl purus in mollis. Vitae et leo duis ut diam. Posuere morbi leo urna molestie at elementum. Fermentum odio eu feugiat pretium nibh. Tellus pellentesque eu tincidunt tortor aliquam nulla. Vitae semper quis lectus nulla at volutpat diam. Diam quis enim lobortis scelerisque fermentum dui faucibus in ornare. Duis tristique sollicitudin nibh sit. Sed euismod nisi porta lorem mollis. Vel pretium lectus quam id leo. Nunc scelerisque viverra mauris in aliquam sem fringilla. Et magnis dis parturient montes nascetur. Ac odio tempor orci dapibus ultrices. Massa id neque aliquam vestibulum morbi. Nunc aliquet bibendum enim facilisis. Interdum posuere lorem ipsum dolor sit amet consectetur.
''')
        self.lni.text += t
        self.ti.text += t


class ExampleApp(App):

    def build(self):
        return ExampleRoot()


ExampleApp().run()
