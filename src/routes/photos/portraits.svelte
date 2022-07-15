<script>
    import GalleryPage from "../../components/gallery/GalleryPage.svelte";

    let imagePaths = [
        '../images/photos/portraits/IMG_8492.jpg',
        '../images/photos/portraits/IMG_8455.jpg',
        '../images/photos/portraits/IMG_8423.jpg'
        ]
</script>
<GalleryPage {imagePaths} title="PORTRAITS STUDIO"/>