<script>
    import MediaQuery from "svelte-media-query";
    import {slide} from "svelte/transition";

    let hidden = true;

    const toggleNav = () => {
        hidden = !hidden;
    };
    $: symbol = hidden ? "▼" : "▲";
</script>

<MediaQuery query="(max-width: 1100px)" let:matches>
    {#if matches}
        {#if !hidden}
            <nav transition:slide style="padding: 10px;">
                <a href="/">ABOUT</a>
                <a href="/photos">PHOTOS</a>
                <a href="/viedoes">VIDEOS</a>
                <a href="/documentaries">DOCUMENTARIES</a>
                <a href="/land_art">LAND ART</a>
                <a href="/textile">TEXTILE</a>
                <a href="/radio">RADIO</a>
                <a href="/project">PROJECTS</a>
                <a href="/contact_me">CONTACT ME</a>
                <a href="/cv">CV</a>
            </nav>
        {/if}
        <button on:click={toggleNav}>{symbol}</button>
    {:else}
        <nav>
            <a href="/">ABOUT</a>
            <a href="/photos">PHOTOS</a>
            <a href="/viedoes">VIDEOS</a>
            <a href="/documentaries">DOCUMENTARIES</a>
            <a href="/land_art">LAND ART</a>
            <a href="/textile">TEXTILE</a>
            <a href="/radio">RADIO</a>
            <a href="/project">PROJECTS</a>
            <a href="/contact_me">CONTACT ME</a>
            <a href="/cv">CV</a>
        </nav>
    
    {/if}
</MediaQuery>


<style>
    nav {
        display: flex;
        justify-content: space-between;
        padding-top: 2%;
        padding-bottom: 5px;
        font-weight: 300;
        width: 100%;
        margin: 0 auto;
        position: relative;
    }

    a:hover {
        color: rgb(200, 0, 0);
        opacity: 0.9;
    }

    button {
        background-color: rgba(238, 238, 238, 0.459);
        margin-top: 10px;
        width: 100%;
    }

    @media(max-width: 1100px) {
        nav {
            flex-direction: column;
        }
    }

</style>