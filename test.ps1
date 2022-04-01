﻿function findWord($substring){
    $path = 'C:\test.txt'
    $content = Get-Content -Path $path;
    for($i = 0; $i -lt $content.Length; $i++){
        $string = $content[$i];
        $separators = @('.', ' ', ',', '/', '?', '!');
        $words = $string.Split($separators);
        foreach ($word in $words){
            if($word.StartsWith($substring) -eq $true){
                echo $word
            }
        }
    }
}

findWord -substring 'te'
