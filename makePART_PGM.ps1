$JAP_ENG = @(
    @("ユーザ名", "UserName"),
    @("連絡先1", "ContactAddress1")
);

$text = @"
str1 = "##JP_KOMOKU##"
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
