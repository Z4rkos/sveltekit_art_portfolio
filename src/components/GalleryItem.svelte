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

    }

    p {
        padding: 0;
        margin: 0;
        overflow: hidden;
        color: #333;
    }

    .container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        margin-bottom: 60px;
        position: relative;
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