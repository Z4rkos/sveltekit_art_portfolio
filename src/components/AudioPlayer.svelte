
<script>

    export let title = "";
    export let src = "";

    let duration;
    let time = 0; 
    let paused = true;

    const togglePlay = () => paused = !paused;

    $: playPauseIcon = paused ? "play_arrow" : "pause";

    
	const format = (seconds) => {
		if (isNaN(seconds)) return '...';

		const minutes = Math.floor(seconds / 60);
		seconds = Math.floor(seconds % 60);
		if (seconds < 10) seconds = '0' + seconds;

		return `${minutes}:${seconds}`;
    }

</script>


<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

<h3>{title}</h3>
<div class="container">
    
    <button on:click={() => paused = !paused} class="playPause">
        <span class="playPauseIcon material-icons">
        {playPauseIcon}
        </span>
    </button>
 
    <div class="timeContainer">
        {format(time)}
    </div>
 
    <input 
        id="progress"

        type="range" 
        min="0" 
        max={duration} 
        bind:value={time} 
        step="1"
    />


<!--
<span id="aVolIco" class="material-icons">volume_up</span>
<input id="aVolume" type="range" min="0" max="1" value="1" step="0.1" disabled/>
 -->
</div>

<audio
    src={src}
    bind:currentTime={time}
    bind:duration
    bind:paused>
</audio>


<style>

    h3 {
        padding-bottom: 10px;
        font-weight: 300;
    }

        /* Materials Icons */
    .material-icons {
        font-size: 28px;
        color: #ffffff;
    }

    /* Container */
    .container {
        margin: auto;
        font-weight: 500;
        display: flex;
        align-items: center;
        box-sizing: border-box;
        max-width: 800px;
        padding: 17px;
        padding-left: 25px;
        margin-bottom: 50px;
        border-radius: 10px;
        background: #484848;
        position: relative;
    }


    /* Play/Puse Button */
    .playPauseIcon {
        padding: 0;
        margin: 0;
        background: 0;
        border: 0;
        cursor: pointer;

        /* Im sure there is a better way to do this, but the bastard refused to be centered otherwise. */
        position: absolute;
        top: 13px;
        padding-right: 10px;
        transform: translateX(-50%);
    }

    /* Time */
    .timeContainer {
        font-size: 14px;
        color: #cbcbcb;
        margin: 0 10px;
    }


    .container input {
        background-color: #222;
        border-radius: 20px;
        width: 100%;
    }

    .container input[type="range"]::-webkit-slider-thumb {
        appearance: none;
    }

    /* Custom Slider Track */
    .container input[type=range]::-webkit-slider-runnable-track {
        background: #8f8f8f;
    }
    .container input[type=range]::-moz-range-track {
        background: #8f8f8f;
    }

    /* Custom Slider Button*/
    .container input[type=range]::-webkit-slider-thumb {
        width: 16px; height: 16px;
        border-radius: 50%;
        border: 0;
        background: #fff;
    }
    .container input[type=range]::-moz-range-thumb {
        width: 16px; height: 16px;
        border-radius: 50%;
        border: 0;
        background: #fff;
    }

    /* (F) VOLUME */
/*     #aVolIco {
    margin: 0 10px;
    } */

</style>