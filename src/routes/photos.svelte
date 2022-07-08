<script>
    import Gallery from "../components/gallery/Gallery.svelte";
    import GalleryItem from "../components/gallery/GalleryItem.svelte";


</script>

<svelte:head>
    <title>Photos</title>
</svelte:head>

<Gallery >
    <GalleryItem 
        href="/photos/the_artist_and_the_frog" 
        title="THE ARTIST AS A FROG. THE FROG AS AN ARTIST" 
        image="images/photos/frog/Frog-marry-2-sm.jpg"
        />
    <GalleryItem 
        href="/photos/geoff_berner" 
        title="GEOFF BERNER: SINGER AND WRITER FROM CANADA"
        image="images/photos/geoff_berner/Geofftri.jpg" 
        />
    <GalleryItem
        href="/photos/portraits"
        title="PORTRAITS STUDIO"
        image="images/photos/portraits/IMG_8492.jpg"
        />
</Gallery>



<style>

</style>
