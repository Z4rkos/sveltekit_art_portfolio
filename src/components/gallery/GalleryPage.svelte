<script>
    export let imagePaths;
    export let title = "";
    export let description = "";

    if (title) title = title.toUpperCase()
</script>  


<div class="container">
    <h1>{title}</h1>
    <p>{description}</p>    
</div>

{#each imagePaths as image}
<img src={image} alt="">
{/each}


<style>
    img {
        margin: auto;
        padding-bottom: 50px;
    }

    h1 {
        font-size: 20px;
        padding: 20px;
        font-weight: 300;
    }
    p {
        font-size: 16px;
        color: #444;
        padding-bottom: 60px;
        font-weight: 300;

    }

    .container {
        max-width: 820px;
        margin: auto;
    }
</style>