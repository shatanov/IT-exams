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
    echo $numI
    if($numI[0] -eq "*"){
       $sep = "to"
     } else {
         if($numI[$numI.Length - 1] -eq "*"){
             $sep = "from"
         }
    }

    $numArr = $numI.Split("*")
    echo $numArr[0]
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


function filterText($f1, $f2, $f3, $f4, $f5){
    $content = Get-Content -Path 'C:\test.txt' -Encoding UTF8;
    $f1 = $f1.Split("=")
    $f2 = $f2.Split("=")
    $f3 = $f3.Split("=")
    $f4 = $f4.Split("=")
    $f5 = $f5.Split("=")
    for($i = 0; $i -lt $content.Length; $i++){
        $string = $content[$i];
        $text = $string.Split("!")
        $col1 = textIncludesFilter -text $text -subStr $f1[1] -argI 0;;
        $col2 = textIncludesFilter -text $text -subStr $f2[1] -argI 1;
        $col3 = numsFilter -text $text -numI $f3[1] -argI 2;
        $col4 = textIncludesFilter -text $text -subStr $f4[1] -argI 3;
        $col5 = textIncludesFilter -text $text -subStr $f5[1] -argI 4;
        if(($col1) -eq $true -and ($col2) -eq $true -and ($col3) -eq $true -and ($col4) -eq $true -and ($col5) -eq $true){
            echo $string
        }
    }

};

filterText $args[0] $args[1] $args[2] $args[3] $args[4]
