<script>
    import Gallery from "../components/gallery/Gallery.svelte";
    import GalleryItem from "../components/gallery/GalleryItem.svelte";
</script>

<svelte:head>
    <title>Documentaries</title>
</svelte:head>

<Gallery>
    <GalleryItem 
        href="documentaries/brakkebygrenda_to_2000"
        title="BRAKKEBYGRENDA TO 2000" 
        image="images/documentaries/brakkebygrenda_to_2000/c.brakkplakat_cropped.jpg"   
    />
    <GalleryItem 
        href="documentaries/brakkebygrenda_to_2014"
        title="BRAKKEBYGRENDA TO 2014" 
        image="images/documentaries/brakkebygrenda_to_2014"   
    />


</Gallery>