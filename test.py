import utils
sps = utils.get_hparams_from_file("model/CN/config.json")["speakers"]

for i in range(len(sps)):
    print(str(i) + " " + sps[i])