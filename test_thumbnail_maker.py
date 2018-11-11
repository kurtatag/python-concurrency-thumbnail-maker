from thumbnail_maker import ThumbnailMakerService

HOST = 'https://dl.dropboxusercontent.com'

IMG_URLS = [
    f'{HOST}/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg',
    f'{HOST}/s/zch88m6sb8a7bm1/pexels-photo-134392.jpeg',
    f'{HOST}/s/lsr6dxw5m2ep5qt/pexels-photo-135130.jpeg',
    f'{HOST}/s/6xinfm0lcnbirb9/pexels-photo-167300.jpeg',
    f'{HOST}/s/2dp2hli32h9p0y6/pexels-photo-167921.jpeg',
    f'{HOST}/s/fjb1m3grcrceqo2/pexels-photo-173125.jpeg',
    f'{HOST}/s/56u8p4oplagc4bp/pexels-photo-185934.jpeg',
    f'{HOST}/s/2s1x7wz4sdvxssr/pexels-photo-192454.jpeg',
    f'{HOST}/s/1gjphqnllzm10hh/pexels-photo-193038.jpeg',
    f'{HOST}/s/pcjz40c8pxpy057/pexels-photo-193043.jpeg',
    f'{HOST}/s/hokdfk7y8zmwe96/pexels-photo-207962.jpeg',
    f'{HOST}/s/k2tk2co7r18juy7/pexels-photo-247917.jpeg',
    f'{HOST}/s/m4xjekvqk4rksbx/pexels-photo-247932.jpeg',
    f'{HOST}/s/znmswtwhcdbpc10/pexels-photo-265186.jpeg',
    f'{HOST}/s/jgb6n4esquhh4gu/pexels-photo-302899.jpeg',
    f'{HOST}/s/rjuggi2ubc1b3bk/pexels-photo-317156.jpeg',
    f'{HOST}/s/cpaog2nwplilrz9/pexels-photo-317383.jpeg',
    f'{HOST}/s/16x2b6ruk18gji5/pexels-photo-320007.jpeg',
    f'{HOST}/s/xqzqzjkcwl52en0/pexels-photo-322207.jpeg',
    f'{HOST}/s/frclthpd7t8exma/pexels-photo-323503.jpeg',
    f'{HOST}/s/7ixez07vnc3jeyg/pexels-photo-324030.jpeg',
    f'{HOST}/s/1xlgrfy861nyhox/pexels-photo-324655.jpeg',
    f'{HOST}/s/v1b03d940lop05d/pexels-photo-324658.jpeg',
    f'{HOST}/s/ehrm5clkucbhvi4/pexels-photo-325520.jpeg',
    f'{HOST}/s/l7ga4ea98hfl49b/pexels-photo-333529.jpeg',
    f'{HOST}/s/rleff9tx000k19j/pexels-photo-341520.jpeg'
]


def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
