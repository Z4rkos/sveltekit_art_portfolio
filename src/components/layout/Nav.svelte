<script>
const test = ['<a href="/">ABOUT</a>', ]
</script>


<nav>
    <a href="/">ABOUT</a>
    <a href="/photos">PHOTOS</a>
    <a href="/">VIDEOS</a>
    <a href="/">DOCUMENTARIES</a>
    <a href="/">LAND ART</a>
    <a href="/">TEXTILE</a>
    <a href="/">RADIO</a>
    <a href="/">PROJECTS</a>
    <a href="/">CONTACT ME</a>
    <a href="/">CV</a>
</nav>

<style>
    nav {
        display: flex;
        justify-content: space-between;
        padding-top: 2%;
        padding-bottom: 2%;
    }

    a:hover {
        color: rgb(200, 0, 0);
        opacity: 0.9;
    }
    @media(max-width: 750px) {
        nav {
            flex-direction: column;
        }
    }
</style>