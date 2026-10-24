$arr = Get-Content -Encoding UTF8 "C:\\Users\\shizu\\OneDrive\\デスクトップ\\python\\generateProdHTML3\\jsonJPElemList.txt" 
$arr2 = Get-Content -Encoding UTF8 "C:\\Users\\shizu\\OneDrive\\デスクトップ\\python\\generateProdHTML3\\jsonENElemList.txt" 

for($i=0; $i -lt $arr.Length; $i++){
    $str1 =  "@(" + '"' + $arr[$i] +  '"' + ","+ '"' + $arr2[$i] + '"' + "),"
    echo $str1
}