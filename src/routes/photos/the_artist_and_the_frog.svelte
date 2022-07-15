<script>
    import GalleryPage from "../../components/gallery/GalleryPage.svelte";

    let imagePaths = [
        '../images/photos/frog/Frog-marry-2-sm.jpg',        
        '../images/photos/frog/frog-as-drunk.jpg',        
        '../images/photos/frog/Frog-ballett-sm.jpg',
        '../images/photos/frog/Frog-as-gartner-sm.jpg',
        '../images/photos/frog/Frog-on-boat-sm.jpg',
        '../images/photos/frog/Dress-pretty-sm.jpg',
        '../images/photos/frog/Afraid-sm.jpg',
        '../images/photos/frog/Lillefrosk-1.-sv-sm.jpg',
        '../images/photos/frog/Toilet2-sm.jpg',
        '../images/photos/frog/Voodoo-2-sm.jpg',
        '../images/photos/frog/Frosk-Red-alle-1-b-w-sm.jpg',
        '../images/photos/frog/Frog-sledge.jpg',
        '../images/photos/frog/teddyfrog-sm.jpg',
        
        ]
</script>
<GalleryPage 
    {imagePaths} 
    title="The artist as a frog- The frog as an artist"
    description={"The artist as a frog- The frog as an artist will be shown for exhibitions as photography and a book. The project are a naive portrait and stories about my selves after I had stroke. The frog feels different and sometimes strange.  But there is humor, irony and sadness in the frogs way of trying new things and how the frog thinks about things. And even if the dreams have changed, there are still.. dreams. The frog also have a beautiful son. Little frog." }/>