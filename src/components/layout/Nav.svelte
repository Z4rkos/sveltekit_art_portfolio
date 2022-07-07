<script>
const test = ['<a href="/">ABOUT</a>', ]
</script>


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

<style>
    nav {
        display: flex;
        justify-content: space-between;
        padding-top: 2%;
        padding-bottom: 2%;
        font-weight: 300;
    }

    a:hover {
        color: rgb(200, 0, 0);
        opacity: 0.9;
    }
    @media(max-width: 1100px) {
        nav {
            flex-direction: column;
        }
    }
</style>