<?php
function fetch_fb_fans($fanpage_name, $no_of_retries = 10, $pause = 500000 /* 500ms */){
    $ret = array();
    // get page info from graph
    $fanpage_data = json_decode(file_get_contents('http://graph.facebook.com/' . $fanpage_name), true);
    if(empty($fanpage_data['id'])){
        // invalid fanpage name
        return $ret;
    }
    $matches = array();
    $url = 'http://www.facebook.com/plugins/fan.php?connections=100&id=' . $fanpage_data['id'];
    $context = stream_context_create(array('http' => array('header' => 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0')));
    for($a = 0; $a < $no_of_retries; $a++){
        $like_html = file_get_contents($url, false, $context);
        preg_match_all('{href="http://www\.facebook\.com/([a-zA-Z0-9._-]+)" data-jsid="anchor" target="_blank"}', $like_html, $matches);
        if(empty($matches[1])){
            // failed to fetch any fans - convert returning array, cause it might be not empty
            return array_keys($ret);
        }else{
            // merge profiles as array keys so they will stay unique
            $ret = array_merge($ret, array_flip($matches[1]));
        }
        // dont get banned as flooder
        usleep($pause);
    }
    return array_keys($ret);
}

print_r(fetch_fb_fans('Airnovapl', 2, 400000));
?>
