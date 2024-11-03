import json
import statistics

if __name__ == "__main__":

    data = json.loads(input())

    keys = data[0].keys()
    # keys = ['name', 'surname', 'marksI', 'marksII', 'marksIII', 'marksIV']
    parts_names = ['marksI', 'marksII', 'marksIII', 'marksIV']

    for key in keys:
        if key in parts_names:

            tmp_data = []
            for i in range(len(data)):
                tmp_data.extend(data[i][key])

            # print(tmp_data)
            
            mark_mean = round(statistics.mean(tmp_data), 1)
            mark_pvariance = round(statistics.pvariance(tmp_data), 1)

            print("%.1f %.1f" % (mark_mean, mark_pvariance))