$JAP_ENG = @(
@("ユーザ名","Username"),
@("連絡先1","Contact1"),
@("連絡先2","Contact2"),
@("連絡先3","Contact3"),
@("連絡先4","Contact4"),
@("連絡先5","Contact5"),
@("休憩所周辺住所","AddressOfTheRestArea"),
@("休憩所周辺住所のGoogleマップ検索アドレス","GoogleMapsSearchAddressOfTheRestArea'sSurroundingAddress"),
@("周辺住所から休憩所まで徒歩何分程度か","HowManyMinutesIsItOnFootFromTheSurroundingAddressToTheRestArea"),
@("休憩一時間当たりの利用料金","UsageFeePerHourForRestArea"),
@("休憩場所の屋根の有無","WhetherTheRestAreaHasARoof"),
@("休憩場所の広さの目安","ApproximateSizeOfTheRestArea"),
@("休憩場所の空調の有無","WhetherTheRestAreaHasAirConditioning"),
@("休憩場所の充電可能コンセントの有無","WhetherTheRestAreaHasChargingOutlets"),
@("外コンセントの口数","NumberOfOutdoorOutlets"),
@("コンセント貸し出し可能時間帯","TimesWhenOutletsAreAvailableForUse"),
@("コンセント貸し出し可能曜日","DaysOfTheWeekWhenOutletsAreAvailableForUse"),
@("最低何日前に事前予約が必要になるかの日数","MinimumNumberOfDaysInAdvanceRequiredForAdvanceReservation"),
@("現在の予約状況のファイルURL","UrlOfTheCurrentReservationStatusFile"),
@("簡易予約状況システムへのURL","URLToTheSimplifiedReservationStatusSystem"),
@("無料の貸し出しKindle端末の有無","AvailabilityOfFreeKindleRentalDevices"),
@("wifiの有無","PresenceOrAbsenceOfWifi"),
@("備考","Note")
);

$text = @"
str1 = "##JP_KOMOKU## : "
str1 += json_dict3["##EN_KOMOKU##"]
str1 += "<br>\n";
f2.write(str1);
"@


foreach($elem1 in $JAP_ENG){

$text2 = $text.Replace("##JP_KOMOKU##", $elem1[0]);
$text2 = $text2.Replace("##EN_KOMOKU##", $elem1[1]);

echo $text2

echo ""


}
