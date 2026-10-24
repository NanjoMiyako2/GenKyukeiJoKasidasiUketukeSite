import json


f3 = open('C:充電受付用サイト情報Jsonファイルが置いてあるパス\\python\\generateProdHTML3\\UserProfJson2.txt','r', encoding='utf-8');
json_dict3 = json.load(f3);


#print(json_dict["1"]["title"])

f2 = open('output1.html', 'w', encoding='utf-8')

str1 = "<hr>\n";
f2.write(str1);

str1 = "ユーザ名 : "
str1 += json_dict3["Username"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先1 : "
str1 += json_dict3["Contact1"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先2 : "
str1 += json_dict3["Contact2"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先3 : "
str1 += json_dict3["Contact3"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先4 : "
str1 += json_dict3["Contact4"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先5 : "
str1 += json_dict3["Contact5"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n";
f2.write(str1);

str1 = "休憩所周辺住所 : "
str1 += json_dict3["AddressOfTheRestArea"]
str1 += "<br>\n";
f2.write(str1);

str1 = "休憩所周辺住所のGoogleマップ検索アドレス : "
str1 += json_dict3["GoogleMapsSearchAddressOfTheRestArea'sSurroundingAddress"]
str1 += "<br>\n";
f2.write(str1);

str1 = "周辺住所から休憩所まで徒歩何分程度か : "
str1 += json_dict3["HowManyMinutesIsItOnFootFromTheSurroundingAddressToTheRestArea"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n";
f2.write(str1);

str1 = "休憩一時間当たりの利用料金 : "
str1 += json_dict3["UsageFeePerHourForRestArea"]
str1 += "<br>\n";
f2.write(str1);

str1 = "休憩場所の屋根の有無 : "
str1 += json_dict3["WhetherTheRestAreaHasARoof"]
str1 += "<br>\n";
f2.write(str1);

str1 = "休憩場所の広さの目安 : "
str1 += json_dict3["ApproximateSizeOfTheRestArea"]
str1 += "<br>\n";
f2.write(str1);

str1 = "休憩場所の空調の有無 : "
str1 += json_dict3["WhetherTheRestAreaHasAirConditioning"]
str1 += "<br>\n";
f2.write(str1);

str1 = "休憩場所の充電可能コンセントの有無 : "
str1 += json_dict3["WhetherTheRestAreaHasChargingOutlets"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n";
f2.write(str1);

str1 = "外コンセントの口数 : "
str1 += json_dict3["NumberOfOutdoorOutlets"]
str1 += "<br>\n";
f2.write(str1);

str1 = "コンセント貸し出し可能時間帯 : "
str1 += json_dict3["TimesWhenOutletsAreAvailableForUse"]
str1 += "<br>\n";
f2.write(str1);

str1 = "コンセント貸し出し可能曜日 : "
str1 += json_dict3["DaysOfTheWeekWhenOutletsAreAvailableForUse"]
str1 += "<br>\n";
f2.write(str1);

str1 = "最低何日前に事前予約が必要になるかの日数 : "
str1 += json_dict3["MinimumNumberOfDaysInAdvanceRequiredForAdvanceReservation"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n";
f2.write(str1);

str1 = "現在の予約状況のファイルURL : "
str1 += json_dict3["UrlOfTheCurrentReservationStatusFile"]
str1 += "<br>\n";
f2.write(str1);

str1 = "簡易予約状況システムへのURL : "
str1 += json_dict3["URLToTheSimplifiedReservationStatusSystem"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n";
f2.write(str1);

str1 = "無料の貸し出しKindle端末の有無 : "
str1 += json_dict3["AvailabilityOfFreeKindleRentalDevices"]
str1 += "<br>\n";
f2.write(str1);

str1 = "wifiの有無 : "
str1 += json_dict3["PresenceOrAbsenceOfWifi"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n";
f2.write(str1);

str1 = "備考 : "
str1 += json_dict3["Note"]
str1 += "<br>\n";
f2.write(str1);


f2.close();
