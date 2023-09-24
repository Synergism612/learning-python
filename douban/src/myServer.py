class MyServer:
    def __init__(self, datasource):
        self.datasource = datasource

    def getTypesCategory(self):
        return self.key_value(self.getTypesMap())

    def getTypesMap(self):
        result = self.getData(8)
        return {k: v for k, v in sorted(result.items(), key=lambda item: -item[1])}

    def getTypesCloud(self):
        return self.name_value(self.getTypesMap())

    def getYear(self):
        result = {}
        for data in self.datasource:
            year = data[2]
            if result.get(year, 0) == 0:
                result[year] = 0
            result[year] = result[year] + 1
        return self.key_value({k: v for k, v in sorted(result.items(), key=lambda item: item[0])})

    def getDuration(self):
        result = {}
        for data in self.datasource:
            duration = data[10]
            if result.get(duration, 0) == 0:
                result[duration] = 0
            result[duration] = result[duration] + 1
        return self.key_value({k: v for k, v in sorted(result.items(), key=lambda item: int(item[0]))})

    def getCountry(self):
        result = self.getData(6)
        copy = result.copy()
        for key, value in copy.items():
            if value < 5:
                if result.get('其它', 0) == 0:
                    result['其它'] = value
                    result.pop(key)
                else:
                    result['其它'] = result['其它'] + value
                    result.pop(key)

        return self.name_value({k: v for k, v in sorted(result.items(), key=lambda item: -item[1])})

    def getData(self, index):
        result = {}
        datasource = self.datasource
        for data in datasource:
            country_value = data[index]
            if '/' in country_value:
                for value in country_value.split('/'):
                    if result.get(value, 0) == 0:
                        result[value] = 0
                    result[value] = result[value] + 1
            else:
                if result.get(country_value, 0) == 0:
                    result[country_value] = 0
                result[country_value] = result[country_value] + 1
        return result

    def getAll(self, number):
        datasource = self.datasource
        result = {
            "total": len(datasource),
            "data": []
        }
        dataList = []
        for data in datasource[(number - 1) * 10:number * 10]:
            dataList.append({
                "id": data[0],
                "movie": data[1],
                "year": data[2],
                "directors": data[3],
                "types": data[8],
                "grade": data[11],
                "votes": data[12],
                "summary": data[13].split()[0],
            })
        result['data'] = dataList
        return result

    def key_value(self, data):
        result = {
            "key": list(data.keys()),
            "value": list(data.values())
        }
        return result

    def name_value(self, data):
        result = []
        for key in data.keys():
            result.append({"name": key, "value": data[key]})
        return result
