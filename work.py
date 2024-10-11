from collections import deque

class StreamingServiceBufferManager:
    def __init__(self):
        # Stack for buffering recent content
        self.recent_content_stack = []
        
        # Queue for video buffering
        self.video_buffer_queue = deque()
        
        # List for available shows
        self.available_shows = []
    
    # Stack Operations for Recent Content
    def add_to_recent_content(self, content):
        """Add content to the recent content stack."""
        self.recent_content_stack.append(content)
    
    def remove_from_recent_content(self):
        """Remove and return the most recent content from the stack."""
        if self.recent_content_stack:
            return self.recent_content_stack.pop()
        return None
    
    def get_recent_content(self):
        """Return the most recent content without removing it."""
        if self.recent_content_stack:
            return self.recent_content_stack[-1]
        return None
    
    # Queue Operations for Video Buffering
    def buffer_video(self, video):
        """Add a video to the video buffer queue."""
        self.video_buffer_queue.append(video)
    
    def play_next_video(self):
        """Remove and return the next video from the buffer queue."""
        if self.video_buffer_queue:
            return self.video_buffer_queue.popleft()
        return None
    
    def get_next_video(self):
        """Return the next video in the buffer queue without removing it."""
        if self.video_buffer_queue:
            return self.video_buffer_queue[0]
        return None
    
    # List Operations for Available Shows
    def add_available_show(self, show):
        """Add a show to the available shows list."""
        self.available_shows.append(show)
    
    def remove_available_show(self, show):
        """Remove a show from the available shows list."""
        if show in self.available_shows:
            self.available_shows.remove(show)
    
    def get_available_shows(self):
        """Return the list of all available shows."""
        return self.available_shows


# Example usage:
manager = StreamingServiceBufferManager()

# Add some shows to the available list
manager.add_available_show("Show 1")
manager.add_available_show("Show 2")
print("Available Shows:", manager.get_available_shows())

# Buffer some videos
manager.buffer_video("Video 1")
manager.buffer_video("Video 2")
print("Next Video in Buffer:", manager.get_next_video())

# Play next video
print("Playing:", manager.play_next_video())

# Add to recent content
manager.add_to_recent_content("Content 1")
manager.add_to_recent_content("Content 2")
print("Most Recent Content:", manager.get_recent_content())

# Remove recent content
print("Removed Recent Content:", manager.remove_from_recent_content())

