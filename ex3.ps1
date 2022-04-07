function findWord(){
    $path = 'C:\test.txt'
    $content = Get-Content -Path $path;
    for($i = 0; $i -lt $content.Length; $i++){
        $arr = @()
        $string = $content[$i];
        $separators = @('.', ' ', ',', '/', '?', '!');
        $words = $string.Split($separators);
        $arr += $words
        booleanFilter -text $arr -bool $true -argI 2;
    }
};

function textIncludesFilter($text, $subStr, $argI){
    $word = $text[$argI]
    if($word.Contains($subStr) -eq $true){
        return $true
    } else {
        return $false
    };
};

function numsFilter($text, $idx, $argI){
    $strNum = $text[$argI]
    $nums = @()
    
};

function booleanFilter($text, $bool, $argI){
   $word = $text[$argI]
   if($word -eq $bool){
       return $true
   } else {
       return $false 
   };

};

findWord
