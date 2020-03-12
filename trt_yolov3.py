# import the necessary packages
import argparse
import random
import os


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--shuffle", required=False,
                    help="shuffle the input images", default="False")
    ap.add_argument('-p', "--path", required=True,
                    help="path to input images")
    args = vars(ap.parse_args())
    return args


def create_subdir(folders):
    for folder in folders:
        os.system(f'mkdir test/{folder}')


def move_images(classes, args):
    for className in classes:
        counter= 0
        images = os.listdir(f'{args["path"]}/{className}/')
        testDatasetSize = round(len(images) * 0.20)
        if args['shuffle'] == "True":
            images = random.sample(images, len(images))

        for image in images:
            if counter < testDatasetSize:
                os.rename(f'{args["path"]}/{className}/{image}', f'test/{className}/{image}')
                counter += 1
        print(f'[{className}] test images are ready.')
    
    os.system(f'mv {args["path"]} train')


def main():
    args = parse_args()
    os.system('mkdir test')
    directories = os.listdir(args['path'])
    create_subdir(directories)
    move_images(directories, args)


if __name__ == '__main__':
    main()
