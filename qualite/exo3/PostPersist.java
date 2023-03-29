package exo3;

public class PostPersist extends Event {

	public PostPersist() {
		super("postPersist");
	}

	public void traiter(EventInterceptor ei, Object entity){
		ei.postPersist(entity);
	}

}
