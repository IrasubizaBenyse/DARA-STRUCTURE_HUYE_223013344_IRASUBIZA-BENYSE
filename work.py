from collections import deque

class StreamingServiceBufferManager:
    def __init__(self):
        # Stack for recently watched content
        self.recent_content = []
        # Queue for video buffering
        self.video_buffer = deque()
        # List for available shows
        self.available_shows = []

    def add_show(self, show):
        """Add a new show to the available shows."""
        self.available_shows.append(show)
        print(f"Added show: {show}")

    def watch_show(self, show):
        """Watch a show, adding it to the recent content stack."""
        if show in self.available_shows:
            self.recent_content.append(show)
            print(f"Watching: {show}")
        else:
            print(f"Show '{show}' is not available.")

    def buffer_video(self, video):
        """Buffer a video by adding it to the video buffer queue."""
        self.video_buffer.append(video)
        print(f"Buffering video: {video}")

    def play_next_video(self):
        """Play the next video from the buffer."""
        if self.video_buffer:
            video = self.video_buffer.popleft()
            print(f"Playing video: {video}")
        else:
            print("No videos in the buffer.")

    def show_recent_content(self):
        """Show recently watched content."""
        print("Recently watched content:")
        for content in reversed(self.recent_content):
            print(content)

    def show_available_shows(self):
        """Display available shows."""
        print("Available shows:")
        for show in self.available_shows:
            print(show)

# Example usage
if __name__ == "__main__":
    manager = StreamingServiceBufferManager()
    
    # Adding available shows
    manager.add_show("Show 1")
    manager.add_show("Show 2")
    manager.add_show("Show 3")
    
    # Displaying available shows
    manager.show_available_shows()
    
    # Watching shows
    manager.watch_show("Show 1")
    manager.watch_show("Show 2")
    
    # Buffering videos
    manager.buffer_video("Video 1")
    manager.buffer_video("Video 2")
    
    # Playing next video
    manager.play_next_video()
    
    # Displaying recent content
    manager.show_recent_content()







     


