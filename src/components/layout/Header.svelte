<script>
    import Nav from "./Nav.svelte";
</script>

<div class="header-container">
    <div class="title-container">
        <a class="title" href="/">ANITA HILLESTAD</a>
        <p>VISUAL ARTIST AND VISUAL ACTIVIST</p>
    </div>
    <Nav />
</div>


<style>

    .header-container {
        margin: 0 auto;
        border-bottom: 1px solid black;
        margin-bottom: 50px;
    }

    .title-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-top: 5%;
    }

    .title {
        font-size: 35px;
        letter-spacing: 0.5em;
    }

</style>