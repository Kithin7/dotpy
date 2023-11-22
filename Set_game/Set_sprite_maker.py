# script to make the set cards from master sprite .png
from PIL import Image

with Image.open('_assets\\set_sprites.png') as im:
    number = ['3', '2', '1']
    fill = ['Hollow', 'Solid', 'Striped']
    color = ['Green', 'Red', 'Purple']
    shape = ['Oval', 'Diamond', 'Squiggle']
    # cards are 35x16 px
    left = 108  # inclusive
    upper = 0  # inclusive
    right = 144  # exclusive?
    lower = 17  # exclusive?

    for col in color:
        for fil in fill:
            for sha in shape:
                for num in number:
                    print((left, upper, right, lower))
                    # new image obj
                    cropped = im.crop((left, upper, right, lower))

                    # save
                    name = num + fil + col + sha
                    cropped.save('_assets\\' + name + '.png')

                    # move crop box
                    upper += 17
                    lower += 17

            # next fill
            # reset upper/lower = 0
            # left/right +36
            upper = 0
            lower = 17
            left += 36
            right += 36
