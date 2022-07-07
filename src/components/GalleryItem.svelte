<script>
    export let title;
    export let image;
    export let href;
</script>


<div class="container">
    <a class="link" href={href}></a>
    <img src={image} alt="">
    <p>{title}</p>
</div>


<style>

    img {
        padding-bottom: 20px;
        transition: opacity 0.4s;
        height: fit-content;

    }

    p {
        padding: 0;
        margin: 0;
        overflow: hidden;
        color: #333;
        font-weight: 300;
    }

    .container {
        min-width: 33%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        position: relative;
        padding-bottom: 5%;
        overflow: hidden;

    }

    .container:hover img {
        opacity: 0.8;
    }

    .link {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: 1;
    }



</style>