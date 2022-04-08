function textIncludesFilter($text, $subStr, $argI){
    if($subStr -eq ""){return $true}
    $word = $text[$argI].ToLower()
    if($word.Contains($subStr.ToLower()) -eq $true){
        return $true
    } else {
        return $false
    };
};

function numsFilter($text, $numI, $argI){
    if($numI -eq ""){return $true}
    $strNum = $text[$argI]
    $num = [float]$strNum
    $sep = "from-to"
    if($numI[0] -eq "*"){
       $sep = "to"
     } else {
         if($numI[$numI.Length - 1] -eq "*"){
             $sep = "from"
         }
    }
    $numArr = $numI.Split(@("*", " "))
    if($sep -eq "to" -and $num -le $numArr[0]){
        return $true
    }

    if($sep -eq "from" -and $num -ge $numArr[0]){
        return $true
    }

    if($sep -eq "from-to" -and $num -le $numArr[1] -and $num -ge $numArr[0]){
        return $true
    }

    return $false 

};

function booleanFilter($text, $bool, $argI){
   if($bool -eq ""){return $true}
   $word = $text[$argI]
   if($word -eq $bool){
       return $true
   } else {
       return $false 
   };

};

function filterText($f1, $f2, $f3, $f4, $f5, $f6){
    $path = 'C:\Users\tshatanov\Desktop\test1.txt'
    $content = Get-Content -Path $path -Encoding UTF8;
    $f1 = $f1.Split("prm1=")
    $f2 = $f2.Split("prm2=")
    $f3 = $f3.Split("prm3=")
    $f4 = $f4.Split("prm4=")
    $f5 = $f5.Split("prm5=")
    $f6 = $f6.Split("prm6=")
    echo $f1
    for($i = 0; $i -lt $content.Length; $i++){
        $string = $content[$i];
        $string = $string -replace "---", '!';
        $text = $string.Split("!")
        $col1 = numsFilter -text $text -numI $f1[0] -argI 0;
        $col2 = textIncludesFilter -text $text -subStr $f2[0] -argI 1;
        $col3 = textIncludesFilter -text $text -subStr $f3[0] -argI 2;
        $col4 = numsFilter -text $text -numI $f4[0] -argI 3;
        $col5 = textIncludesFilter -text $text -subStr $f5[0] -argI 4;
        $col6 = textIncludesFilter -text $text -subStr $f6[0] -argI 5;
        if(($col1) -eq $true -and ($col2) -eq $true -and ($col3) -eq $true -and ($col4) -eq $true -and ($col5) -eq $true -and ($col6) -eq $true){
            echo $string
        }
    }

};

filterText $args[0] $args[1] $args[2] $args[3] $args[4] $args[5]
