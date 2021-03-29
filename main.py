import os
import glob
import csv


# def get_high_lod_name(directory, mtl):
#     base_mtl_name = os.path.basename(mtl)
#     base_name = base_mtl_name[4:-10]
#     semodel_list = glob.glob(directory+"\\" + base_name + "*.semodel")
#     highest_lod = 0
#     semodel_name = ""
#     for semodel in semodel_list:
#         base_semodel = os.path.basename(semodel)
#         lod = base_semodel[-9:-8]
#         if int(lod) > int(highest_lod):
#             highest_lod = lod
#             semodel_name = base_semodel
#     return semodel_name[:-8]


def rename(directory):
    if not (os.path.exists(directory) and os.path.exists(directory + "\\_images")):
        print("Folder's structure is invalid.")
        exit()
    mtl_list = get_mtl_list(directory)
    for mtl in mtl_list:
        mtl_content = parse_mtl(mtl)
        # obj_name = get_high_lod_name(directory, mtl)
        material_to_rename = {"aoMap": "_o", "normalMap": "_n", "glossMap": "_g", "colorMap": "_c", "specColorMap": "_s", "emissiveMap": "_e"}
        for material, filename in mtl_content:
            rename_texture(directory, mtl, material, filename, material_to_rename)


def get_mtl_list(directory):
    return glob.glob(directory+"\\*.txt")


def parse_mtl(mtl):
    mtl_csv = open(mtl, 'r')
    return csv.reader(mtl_csv)


def rename_texture(directory, mtl_path, material_type, texture_file_name, material_to_rename):
    if material_type not in material_to_rename.keys():
        print(material_type + " is irrelevant. Skipped.")
        return
    if not os.path.exists(directory + "\\_images\\" + texture_file_name + ".png"):
        print(texture_file_name + " doesn't exist. Skipped.")
        return
    os.rename(directory + "\\_images\\" + texture_file_name + ".png", directory + "\\_images\\" + os.path.basename(mtl_path)[:-4] + material_to_rename[material_type] + ".png")
    print(texture_file_name + ".png" + " renamed to " + os.path.basename(mtl_path)[:-4] + material_to_rename[material_type] + ".png")


def main():
    directory = input("Enter folder's full path:")
    rename(directory)


if __name__ == "__main__":
    # execute only if run as a script
    main()

# pyinstaller --onefile main.py -n rename_textures.exe